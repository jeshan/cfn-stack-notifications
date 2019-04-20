import json
import sys
from glob import glob
from subprocess import check_output, CalledProcessError

import yaml


def run(command):
    print('Running', command)
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output.decode('utf-8'))


def _configure_profile(profile_name, profile_role):
    print('Got', profile_role, 'for', profile_name)
    if profile_name != 'default':
        profile_name = f'profile.{profile_name}'
    run(f'aws configure set {profile_name}.region us-east-1')
    run(f'aws configure set {profile_name}.credential_source EcsContainer')
    run(f'aws configure set {profile_name}.role_arn {profile_role}')


def go(repo):
    for path in glob('config/*/config.yaml'):
        profile_name = yaml.load(open(path))['profile']
        env = path[path.index('/') + 1:]
        env = env[:env.index('/')]
        key_path = f'{env}/base'
        outputs_list = json.loads(run(f'sceptre --ignore-dependencies --output json list outputs {key_path}.yaml'))
        print(outputs_list)
        role = None
        for output_group in outputs_list:
            for key, outputs in output_group.items():
                for output in outputs:
                    if output['OutputKey'] == 'TargetRole':
                        role = output['OutputValue']
                        _configure_profile(profile_name, role)
        if not role:
            raise Exception(f'Role for {profile_name} not found in stack {key_path}, aborting.')
    _configure_profile(repo, 'default')


if __name__ == '__main__':
    go(sys.argv[1])
