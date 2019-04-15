import sys

regions = 'us-east-1,us-east-2,eu-west-1,us-west-1,us-west-2,ap-south-1,ap-southeast-1,ap-southeast-2,ca-central-1,eu-central-1,eu-north-1,eu-west-2,eu-west-3,sa-east-1,ap-northeast-1,ap-northeast-2,ap-northeast-3'.split(
    ',')


def go(env):
    for region in regions:
        with open(f'config/{env}/{region}.yaml', 'w') as f:
            f.write(f"""template_path: template.yaml
region: {region}
""")


if __name__ == '__main__':
    go(sys.argv[1])
