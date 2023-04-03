from twisted.internet import reactor

from twisted.internet.protocol import ServerFactory, Protocol
from twisted.internet.endpoints import serverFromString
from twisted.application.service import Application
from twisted.application.internet import TCPServer

class randomServer(Protocol):
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def connectionLost(self, reason):
        print(reason)
        
    def dataReceived(self, data):
        print(data)

class randomFactory(ServerFactory):
    proto = randomServer
    
    def buildProtocol(self, addr):
        return self.proto()
            
endpoint = serverFromString(reactor, "tcp:4005")
protocol=Protocol()

application = Application("Something")
service = TCPServer(4005, randomFactory())

service.setServiceParent(application)
