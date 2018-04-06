#!/usr/bin/python

from fabric.api import cd, env, prefix, run, task

env.hosts = ['localhost']

@task
def memory_usage():
    run('free -m')

@task
def deploy():
    with cd('/var/www/project-env/project'):
        with prefix('. ../bin/activate'):
            run('git pull')
            run('touch app.wsgi')

