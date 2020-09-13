from invoke import task


@task
def test(c, env='prod', lang='en', app='android', device='emulator'):
    c.run(f'python3 -m pytest src/spec/{app}/login_test.py --app={app} --device={device}')
