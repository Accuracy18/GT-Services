from general_stuff import *
import json

class randomServer(Protocol):
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def connectionMade(self):
        pass
        
    def connectionLost(self, reason):
        print(reason)
        
    def dataReceived(self, data):
        data = json.dumps(data.decode().split('\n')[0])

class randomFactory(ServerFactory):
    proto = randomServer
    
    def buildProtocol(self, addr):
        return self.proto()
            
endpoint = serverFromString(reactor, "tcp:4005")
protocol=Protocol()

random_service = TCPServer(4005, randomFactory())
