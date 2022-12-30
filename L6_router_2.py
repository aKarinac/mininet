from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel,info
from mininet.cli import CLI

class LinuxRouter(Node):
	def config(self, **params):
		super(LinuxRouter,self).config(**params)
		self.cmd('sysctl net.ipv4.ip_forward=1')

	def terminate(self):
		self.cmd('sysctl net.ipv4.ip_forward=0')
		super(LinuxRouter,self).terminate()


class NetworkTopo(Topo):
	def build(self, **_opts):
		defaultIP = '10.0.1.1/24'
		router = self.addNode('r0',cls=LinuxRouter,ip=defaultIP)
		h1 = self.addHost('h1', ip='10.0.1.2/24',defaultRoute='via 10.0.1.1')
		h2 = self.addHost('h2', ip='10.0.2.2/24',defaultRoute='via 10.0.2.1')
		h3 = self.addHost('h3', ip='10.0.2.3/24',defaultRoute='via 10.0.2.1')

		s1 = self.addSwitch('s1')

		self.addLink(h1,router,intfName2='r0-eth1',params2={'ip' : '10.0.1.1/24'})
		self.addLink(h2,router,intfName2='r0-eth2',params2={'ip' : '10.0.2.1/24'})

		self.addLink(h2,s1)
		self.addLink(h3,s1)

def run():
	topo = NetworkTopo()
	net = Mininet(topo=topo)
	net.start()
	info('*** Routing Table on Router:\n')
	print (net['r0'].cmd('route'))
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	run()

