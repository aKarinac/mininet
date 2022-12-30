from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def emptyNet():
	net = Mininet(controller = Controller)
	info('*** Adding controller\n')
	net.addController('c0')
	
	info('*** Adding hosts\n')
	h1 = net.addHost('h1', ip = '172.3.30.1')
	h2 = net.addHost('h2', ip = '172.3.30.2')
	h3 = net.addHost('h3', ip = '172.3.30.3')
	h4 = net.addHost('h4', ip = '172.3.30.4')
	
	info('*** Adding switch\n')
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	info('*** Creating links\n')
	net.addLink(h1,s1)
	net.addLink(h2,s1)
	net.addLink(h3,s2)
	net.addLink(h4,s2)
	net.addLink(s1,s2)
	
	info('*** Starting network\n')
	net.start()

	
	info('*** Running CLI\n')
	CLI(net)
	
	info('*** Stopping network')
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	emptyNet()
