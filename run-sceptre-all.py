import sys
from glob import glob
from subprocess import check_output, CalledProcessError

fail_count = 0


def run(command):
    global fail_count
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        print(output)
    except CalledProcessError as exc:
        print("Status : FAIL while running", command, exc.returncode, exc.output.decode('utf-8'))
        fail_count += 1


def go():
    for path in glob('config/*'):
        if '.' not in path:
            env = path[path.rindex('/') + 1:]
            run(f'sceptre --no-colour delete -y {env}')


if __name__ == '__main__':
    go()
    sys.exit(fail_count)
