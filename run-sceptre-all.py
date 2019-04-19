from glob import glob
from subprocess import check_output


def run(command):
    output = check_output(command.split(' ')).decode('utf-8')
    print(output)


def go():
    for path in glob('config/*'):
        if '.' not in path:
            env = path[path.rindex('/') + 1:]
            run(f'sceptre --no-colour launch -y {env}')


if __name__ == '__main__':
    go()
