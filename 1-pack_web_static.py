#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the  AirBnB Clone repo, using the
function do_pack.
"""
from fabric.api import *
from fabric.api import local
from datetime import datetime
import os
def do_pack():
    '''generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    result = local("tar -cvzf {} -C web_static .".format(path))

    if result.failed:
        return None
    return path
