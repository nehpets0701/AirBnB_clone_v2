#!/usr/bin/python3
"""first fabric"""
from datetime import datetime
from fabric.api import local, run, env, put
import os


env.hosts = ["35.227.109.238", "34.73.167.95"]


def do_pack():
    """pack function"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(time))
    except:
        return None
    return "versions/web_static_{}.tgz web_static".format(time)


def do_deploy(archive_path):
    """deploy function"""
    if os.path.exists(archive_path) is False:
        return False
    archive = archive_path.split('/')[1]
    unpack = archive.split('.')[0]
    target = "/data/web_static/releases/{}/".format(archive, unpack)
    try:
        put(archive_path, "/tmp/{}".format(archive))
        run("mkdir -p {}".format(target))
        run("tar -xzf /tmp/{} -C {}".format(archive, target))
        run("rm /tmp/{}".format(archive))
        run("mv {}web_static/* {}".format(target, target))
        run("rm -rf {}web_static/".format(target))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(target))
    except:
        return False
    return True
