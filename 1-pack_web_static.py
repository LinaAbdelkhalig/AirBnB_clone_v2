#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the
function do_pack
"""


from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        f = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(f))
        return f
    except Exception:
        return None
