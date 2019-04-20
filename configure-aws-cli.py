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
        parsed = yaml.load(open(path))
        profile_name = parsed['profile']
        account_id = parsed['account_id']
        _configure_profile(profile_name, f'arn:aws:iam::{account_id}:role/cfn-stack-notifications-target')
    _configure_profile(repo, 'default')


if __name__ == '__main__':
    go(sys.argv[1])
