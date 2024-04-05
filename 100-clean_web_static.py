#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives
"""


from fabric.api import cd, local, run
from os import listdir


def do_clean(number=0):
    """deletes out-of-date archives"""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    vers = sorted(listdir("versions"))
    for i in range(number):
        vers.pop()

    with cd("/data/web_static/releases"):
        vers = run("ls -tr").split()
        vers = [v for v in vers if "web_static_" in v]
        for i in range(number):
            vers.pop()
        for v in vers:
            run("rm -rf ./{}".format(v))
