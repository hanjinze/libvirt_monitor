# vim: tabstop=4 shiftwidth=4 softtabstop=4
import libvirt,os,sys,re
from xml.etree import ElementTree

def get_devices(dom,path,devs):
	tree=ElementTree.fromstring(dom.XMLDesc(0))
	devices=[]
	for target in tree.findall(path):
		dev=target.get(devs)
		if not dev in devices:
			devices.append(dev)
	return devices

def get_memory(pid):
    mem=0
    for line in file('/proc/%d/smaps' % int(pid),'r'):
        if re.findall('Private_',line):
            mem+=int(re.findall('(\d+)',line)[0])
    return mem
