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

# This code is used to get facts and HW information form Juniper device in jason format

from jnpr.junos import Device
from pprint import pprint
from lxml import etree
import json

# we can use context manager to avoid open or close the connection in above method
# so we will use above or below method


if __name__ == "__main__":

    dev = Device(host='192.168.26.210', user='lab', passwd='lab123')
    dev.open()
    #pprint (dev.facts)
    get_facts_json = dev.rpc.get_config(filter_xml="interfaces", options={"format": "json"})
    dev.close()
    pprint (get_facts_json)

