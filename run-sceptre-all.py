from glob import glob
from subprocess import check_output, CalledProcessError


def run(command):
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        print(output)
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output.decode('utf-8'))


def go():
    for path in glob('config/*'):
        if '.' not in path:
            env = path[path.rindex('/') + 1:]
            run(f'sceptre --no-colour launch -y {env}')


if __name__ == '__main__':
    go()
