from general_stuff import *

app = Klein()

@app.route('/')
def something(request):
    return b'555'

application = Application("Something")
service = TCPServer(4006, Site(app.resource()))

service.setServiceParent(application)