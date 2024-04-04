#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers
"""


from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists, isdir

# IP addresses of the servers where the archive will be sent
env.hosts = ["54.84.48.73", "100.26.173.120"]


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        f = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(f))
        return f
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    # False, if the file at archive_path doesn't exist
    if exists(archive_path) is False:
        return False
    try:
        # filename
        f = archive_path.split("/")[-1]
        # remove the extension from the filename
        fn = f.split(".")[0]
        # the folder where the archive will be uncompressed
        folder = "/data/web_static/releases/"

        # upload the archive to /tmp/
        put(archive_path, "/tmp/{}".format(f))
        run("rm -rf {}{}/".format(folder, fn))
        # create the directory and uncompress to the web server
        run("mkdir -p {}{}/".format(folder, fn))
        run("tar -xzf /tmp/{} -C {}{}/".format(f, folder, fn))
        # delete the archive from the web server
        run("rm /tmp/{}".format(f))
        # move the files from web_static to the parent folder
        run("mv {0}{1}/web_static/* {0}{1}/".format(folder, fn))
        run("rm -rf {}{}/web_static".format(folder, fn))
        # remove the symbolic link /data/web_static/current from the server
        run("rm -rf /data/web_static/current")
        # create a new symbolic link /data/web_static/current on the server
        run("ln -s {}{}/ /data/web_static/current".format(folder, fn))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
