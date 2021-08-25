#!/usr/bin/python3
"""
generates a .tgz archive from the contents
of the web_static folder of your AirBnB
Clone repo, using the function do_pack
and deploy on server
"""
from datetime import datetime
from genericpath import exists
from fabric.api import local, put, run, env
import os


env.hosts = ['18.234.233.93', '35.243.205.77']


def do_pack():
    """generate a tar.gz archive with fabric"""
    date = datetime.now()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day, date.hour, date.minute, date.second)
    local("mkdir -p versions")
    cmd = local("tar -vczf {} web_static".format(archive_name))
    if cmd.succeeded:
        return archive_name
    else:
        return None


def do_deploy(archive_path):
    """deploy archive"""
    if os.path.exists(archive_path) is False:
        return False
    file_name = archive_path.split("/")[-1]
    file_name_wthout_ext = file_name.split(".")[0]
    data_path = "/data/web_static/releases"
    try:
        put(archive_path, '/tmp/{}'.format(file_name))
        run("mkdir -p {}/{}/".format(data_path, file_name_wthout_ext))
        run("tar -xzf /tmp/{} -C {}/{}/".format(
            file_name, data_path, file_name_wthout_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/{}/web_static/* {}/{}/".format(
            data_path, file_name_wthout_ext, data_path, file_name_wthout_ext))
        run("rm -rf {}/{}/web_static".format(data_path, file_name_wthout_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(
            data_path, file_name_wthout_ext))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
