#!/usr/bin/python3
from fabric.api import *
from os.path import exists

env.hosts = ['54.236.47.254', '52.91.133.233']

def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_file = archive_path.split('/')[-1]
        archive_folder = "/data/web_static/releases/{}".format(
            archive_file.split('.')[0])

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(archive_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, archive_folder))
        run("rm /tmp/{}".format(archive_file))
        run("mv {}/web_static/* {}".format(archive_folder, archive_folder))
        run("rm -rf {}/web_static".format(archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_folder))

        return True

    except:
        return False
