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

# This code is used to add config from file as set commands to juniper device and return if there is error


from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
from time import sleep

# mode can be private/dynamic/exclusive/batch/ephemeral
# here we add commands to file and commit all in one step


try:
    dev = Device(host='192.168.8.20', user='lab', passwd='lab123')
    dev.open()
    new_commands = Config(dev, mode='exclusive')
    new_commands.load(path="junoscommands.txt", format='set' , merge=True)
    diff_config = new_commands.diff()
    if diff_config is None:
        print ('Configuration already up to date')
    else:
        print (diff_config)
        new_commands.commit()
		sleep (2)
        print ('Configuration applied')
except ConnectAuthError:
    print ('ConnectAuthError due to wrong login')
except ConnectTimeoutError:
    print ('ConnectTimeoutError due to device not reachable')
except ConnectError as error:
    print ('"due to" + error ')
except ConfigLoadError:
    print ("config file is corrupted, problem to load")
except Exception as error:
    print ('"due to" + error ')
finally:
    dev.close()