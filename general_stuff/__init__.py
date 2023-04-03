from twisted.internet.protocol import ServerFactory, Protocol
from twisted.internet.endpoints import serverFromString
from twisted.application.service import Application
from twisted.application.internet import TCPServer
from twisted.internet import reactor
from twisted.web.server import Site
from klein import Klein

application = Application("Something")