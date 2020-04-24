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

# This code is used to get no of BGP peers up and down


from jnpr.junos import Device

# we can use method 1 or method 2

###method 1

###peers_established = 0
###
###peers_down = 0
###
###with Device(host='192.168.16.30', user='lab', passwd='lab123') as dev:
###
###	bgp_summery = dev.rpc.get_bgp_summary_information()
###	bgp_peers_states = bgp_summery.xpath("bgp-peer/peer-state")
###
###for peer_state in bgp_peers_states:
###    if peer_state == "established":
###        peers_established +=1
###    else:
###        peers_down +=1
###
###print ("peers up count is {} and peer down count is {} and total no of peers is {}".format(peers_established, peers_down, peers_established+peers_down))
###
###if peers_down != 0:
###    print ("Warning there is peers in down state !")
###exit(1)


# method 2

peers_established = 0
peers_down = 0

dev = Device(host='192.168.66.40', user='lab', passwd='lab123')

dev.open()
bgp_summery = dev.rpc.get_bgp_summary_information()
bgp_peers_states = bgp_summery.xpath("bgp-peer/peer-state")

for peer_state in bgp_peers_states:
    if peer_state == "established":
        peers_established +=1
    else:
        peers_down +=1
dev.close()

print ("peers up count is {} and peer down count is {} and total no of peers is {}".format(peers_established, peers_down, peers_established+peers_down))

if peers_down != 0:
    print ("Warning there is peers in down state !")
    exit(1)
  
    


