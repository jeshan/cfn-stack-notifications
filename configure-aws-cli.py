import sys
from glob import glob
from subprocess import check_output

import boto3
import yaml


def _configure_profile(profile_name, profile_role):
    check_output(f'aws configure set profile.{profile_name}.region us-east-1')
    check_output(f'aws configure set profile.{profile_name}.credential_source EcsContainer')
    check_output(f'aws configure set profile.{profile_name}.role_arn {profile_role}')


def configure_profile(client, repo, profile_name):
    name = f'/github.com/{repo}/aws-profile-roles/{profile_name}'
    print(f'Getting parameter {name}')
    role = client.get_parameter(Name=name)['Parameter']['Value']
    _configure_profile(profile_name, role)


def go(repo):
    client = boto3.client('ssm')
    for path in glob('config/*/config.yaml'):
        profile_name = yaml.load(open(path))['profile']
        configure_profile(client, repo, profile_name)
    configure_profile(client, repo, 'default')


if __name__ == '__main__':
    go(sys.argv[1])
