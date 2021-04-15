#!/usr/bin/python3
"""first fabric"""
""" 1-pack_web_static.py """
from datetime import datetime
from fabric.api import local


def do_pack():
    """pack function"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(time))
    except:
        return None
    return "versions/web_static_{}.tgz web_static".format(time)
