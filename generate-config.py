import os
import sys
from os import mkdir
from os.path import exists

from mako.template import Template

regions = 'us-east-1,us-east-2,eu-west-1,us-west-1,us-west-2,ap-south-1,ap-southeast-1,ap-southeast-2,ca-central-1,eu-central-1,eu-north-1,eu-west-2,eu-west-3,sa-east-1,ap-northeast-1,ap-northeast-2'.split(
    ',')


def _mkdir(path):
    try:
        mkdir(path)
    except:
        pass


def save_template_file(path, data, directory=None):
    basename = path[(path.rindex('/') + 1) if '/' in path else 0:]
    with open(path if not directory else f'{directory}/{basename}', 'w') as f:
        src = path[:path.rindex('.') + 1] + 'template.' + path[path.rindex('.') + 1:]
        f.write(Template(filename=src).render(**data))


def go(env):
    account_id = os.environ['ACCOUNT_ID']
    project_name = os.environ['PROJECT_NAME']
    public_bucket = os.environ.get('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    private_bucket = os.environ.get('PRIVATE_BUCKET', 'jeshan-oss-private-files')

    _mkdir('config/app/deployment')

    _mkdir('config')
    _mkdir('config/app/')
    _mkdir('config/app/deployment')
    _mkdir(f'config/app/{env}')
    if not exists(f'config/app/{env}/config.yaml'):
        with open(f'config/app/{env}/config.yaml', 'w') as f:
            f.write(f"""profile: {env}
""")

    with open('config/config.yaml', 'w') as f:
        f.write(f"""project_code: {project_name}
region: us-east-1
""")

    with open('config/app/deployment/pipeline.yaml', 'w') as f:
        f.write(f"""template_path: deployment-pipeline.yaml

parameters:
  ProjectName: {project_name}
  PrivateBucket: {private_bucket}
  PublicBucket: {public_bucket}
""")

    with open(f'config/app/{env}/base.yaml', 'w') as f:
        f.write(f"""template_path: deployment-target-account.yaml

parameters:
  DeploymentAccount: {account_id}
  ProjectName: {{{{stack_group_config.project_code}}}}
""")
    for region in regions:
        with open(f'config/app/{env}/{region}.yaml', 'w') as f:
            f.write(f"""template_path: template.yaml

region: {region}
""")


if __name__ == '__main__':
    env_name = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    go(env_name)
