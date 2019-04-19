import sys
from glob import glob
from subprocess import check_output, CalledProcessError

import boto3
import yaml


def run(command):
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        print(output)
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)


def _configure_profile(profile_name, profile_role):
    print('Got', profile_role, 'for', profile_name)
    run(f'aws configure set profile.{profile_name}.region us-east-1')
    run(f'aws configure set profile.{profile_name}.credential_source EcsContainer')
    run(f'aws configure set profile.{profile_name}.role_arn {profile_role}')


def configure_profile(repo, profile_name, parameters):
    name = f'/github.com/{repo}/aws-profile-roles/{profile_name}'
    role = None
    for param in parameters:
        if param['Name'] == name:
            role = param['Value']
            _configure_profile(profile_name, role)
    if not role:
        raise Exception(f'Role for {profile_name} not found at {profile_name}, aborting.')


def go(repo):
    client = boto3.client('ssm')
    parameters = client.get_parameters_by_path(Path=f'/github.com/{repo}', Recursive=True)['Parameters']
    for path in glob('config/*/config.yaml'):
        profile_name = yaml.load(open(path))['profile']
        configure_profile(repo, profile_name, parameters)
    configure_profile(repo, 'default', parameters)


if __name__ == '__main__':
    go(sys.argv[1])
