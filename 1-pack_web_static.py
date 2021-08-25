#!/usr/bin/python3
"""
generates a .tgz archive from the contents
of the web_static folder of your AirBnB
Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generate a tar.gz archive with fabric"""
    date = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day, date.hour, date.minute, date.second)
    local("mkdir -p versions")
    cmd = local("tar -vczf {} web_static".format(archive_path))
    if cmd.succeeded:
        return archive_path
    else:
        return None
