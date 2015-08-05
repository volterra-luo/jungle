# -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

import server_config

env.hosts = ['']
env.hosts.append(server_config.HOST)

def test():
    with settings(warn_only=True):
        result = local('./manage.py test jungle', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    code_dir = server_config.CODE_DIR
    code_repo = server_config.CODE_REPO
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone %s %s" % (code_repo, code_dir) )
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")

def host_type():
    run('uname -s')