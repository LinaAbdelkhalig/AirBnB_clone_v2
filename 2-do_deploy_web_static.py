#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers
"""


from fabric.api import put, run, env
from os.path import exists

# IP addresses of the servers where the archive will be sent
env.hosts = ["54.84.48.73", "100.26.173.120"]


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
        put(archive_path, "/tmp/")
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
