#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the  AirBnB Clone repo, using the
function do_pack.
"""
from fabric.api import *
from datetime import datetime
from fabric.decorators import runs_once
from fabric.api import local
import os


def do_pack():
    '''using web static content to generate archive'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    result = local("tar -cvzf {} -C web_static .".format(path))

    if result.failed:
        return None
    return path
