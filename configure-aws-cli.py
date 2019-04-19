import sys
from glob import glob
from subprocess import check_output

import boto3
import yaml


def _configure_profile(profile_name, profile_role):
    print('Got', profile_role, 'for', profile_name)
    check_output(f'aws configure set profile.{profile_name}.region us-east-1')
    check_output(f'aws configure set profile.{profile_name}.credential_source EcsContainer')
    check_output(f'aws configure set profile.{profile_name}.role_arn {profile_role}')


def configure_profile(repo, profile_name, parameters):
    name = f'/github.com/{repo}/aws-profile-roles/{profile_name}'
    for param in parameters:
        if param['Name'] == name:
            _configure_profile(profile_name, param['Value'])


def go(repo):
    client = boto3.client('ssm')
    parameters = client.get_parameters_by_path(Path=f'/github.com/{repo}', Recursive=True)['Parameters']
    for path in glob('config/*/config.yaml'):
        profile_name = yaml.load(open(path))['profile']
        configure_profile(repo, profile_name, parameters)
    configure_profile(repo, 'default', parameters)


if __name__ == '__main__':
    go(sys.argv[1])
