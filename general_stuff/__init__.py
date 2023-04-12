from twisted.internet.protocol import ServerFactory, Protocol
from twisted.internet.endpoints import serverFromString
from twisted.application.service import Application
from twisted.application.internet import TCPServer
from twisted.internet import reactor
from twisted.web.server import Site
from klein import Klein

from general_stuff.randombox.server import random_service
from general_stuff.http_server.server import http_service

application = Application("Something")

random_service.setServiceParent(application)
http_service.setServiceParent(application)