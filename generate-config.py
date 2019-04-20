import sys
import os

regions = 'us-east-1,us-east-2,eu-west-1,us-west-1,us-west-2,ap-south-1,ap-southeast-1,ap-southeast-2,ca-central-1,eu-central-1,eu-north-1,eu-west-2,eu-west-3,sa-east-1,ap-northeast-1,ap-northeast-2'.split(
    ',')


def go(env):
    open(f'config/{env}/config.yaml', 'w')
    with open(f'config/{env}/base.yaml', 'w') as f:
        f.write(f"""template_path: deployment-target-account.yaml

parameters:
  DeployerRole: arn:aws:iam::{os.environ['ACCOUNT_ID']}:role/service-role/cfn-stack-notifications-deployer
  DlqName: {{{{stack_group_config.dlq_name}}}}
  EventsTopicName: {{{{stack_group_config.events_topic_name}}}}
""")
    for region in regions:
        with open(f'config/{env}/{region}.yaml', 'w') as f:
            f.write(f"""template_path: template.yaml
region: {region}

parameters:
  Role: !stack_output {env}/base.yaml::FnRole
  TopicName: {{{{stack_group_config.events_topic_name}}}}
""")


if __name__ == '__main__':
    go(sys.argv[1])
