#!/usr/bin/python3
""" tar fabfile """

from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """ creates tar file for websatic """

    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    date_str = date_str.replace('/', '')

    if not os.path.exists('versions'):
        local("mkdir versions")
    file_ = "versions/web_static_{}.tgz".format(date_str)
    result = local("tar -cvzf {} web_static".format(file_))

    if result.succeeded:
        file_
    else:
        return None
