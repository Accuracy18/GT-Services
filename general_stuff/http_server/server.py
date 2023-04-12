from general_stuff import *

app = Klein()

@app.route('/')
def something(request):
    return b'555'

http_service = TCPServer(4006, Site(app.resource()))