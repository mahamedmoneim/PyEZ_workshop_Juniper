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

# This code is used to add config from file as set commands to juniper device or command line by different methods

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='192.168.146.250', user='netconf', passwd='netconf123') as dev:

    
# we can use method 1 (commands one by one) or method 2 all in one step as list of commands or method three by file contains all commands

#method 1
# mode can be private/dynamic/exclusive/batch/ephemeral
# here we add commands line by line and commit all commands one time
#     with Config(dev, mode='exclusive') as new_commands:
#         new_commands.load('set interfaces ge-0/0/2 description DNS-zzz',
#                 format='set')
#         new_commands.load('set interfaces ge-0/0/3 description DNS-yyy',
#                 format='set')
#         new_commands.load('set interfaces ge-0/0/4 description DNS-www',
#                 format='set')
#         diff_config = new_commands.diff()
#         if diff_config is None:
#             print ('Configuration already up to date')
#         else:
#             print (diff_config)
#             new_commands.commit()


#method 2
# we can load all commands in one list instead add them line by line but commit will be done for each command
    commands = ['set interfaces ge-0/0/2 description DNS-sit2222','set interfaces ge-0/0/3 description DNS-site333','set interfaces ge-0/0/4 description DNS-site444']
    for command_line in commands:
        print ('we will add command' +" " + command_line + " " +'to the router')
        with Config(dev, mode='exclusive') as new_commands:
            new_commands.load(command_line,
                    format='set')
            diff_config = new_commands.diff()
            if diff_config is None:
                print ('Configuration already up to date')
            else:
                print (diff_config)
                new_commands.commit()
				
				
#method 3 file contains all commands

#    new_commands = Config(dev, mode='exclusive')
#    new_commands.load(path="junoscommands.txt", format='set' , merge=True)
#    diff_config = new_commands.diff()
#    if diff_config is None:
#        print ('Configuration already up to date')
#    else:
#        print (diff_config)
#        new_commands.commit()
#        print ('Configuration applied')