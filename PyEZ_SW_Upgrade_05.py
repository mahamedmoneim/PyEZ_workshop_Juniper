#!/user/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sat 4 April 2020
@author: Mohamed Abd-moneim
"""

"""
Junos PyEZ is a Python library that enables you to manage and automate devices running Junos OS.
Reference
#https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/installation/junos-pyez-server-installing.html
https://www.juniper.net/documentation/product/en_US/junos-pyez
https://github.com/Juniper/py-junos-eznc

# you need to install Python 3 on your PC first to run the code and you can edit code by notepad++ or any text editor
# to install needed packages on linux you connect machine to internet and run below commands to install packages which are used in code

### for Linux
pip3 install git+https://github.com/Juniper/py-junos-eznc.git
pip3 install junos-eznc
### for windows
py -m pip install ecdsa
py -m pip install junos-eznc
py -m pip install git+https://github.com/Juniper/py-junos-eznc.git

### for Windows
py -m pip install ecdsa
py -m pip install junos-eznc
py -m pip install git+https://github.com/Juniper/py-junos-eznc.git

"""

# This code is used to upgrade Juniper device software and reboot

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

NEW_PACKAGE = "/var/tmp/junos-19.1R1.10.tgz"

def progress_callback(dev, report):
    print (report)
	

with Device(host='192.168.146.250', user='netconf', passwd='netconf123') as dev:
    sw = SW(dev)
ok = sw.install(package=NEW_PACKAGE, no_copy=True, validate=False, progress=progress_callback)
sw.reboot()

