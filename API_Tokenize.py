from tornado import httpserver
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import tornado
import sys
import json


from Tokenize import *
from config import *

class MainHandler(RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def get(self):
        result = {"success": True, "output": "This is the main handlers"}
        self.write(json.dumps(result))

class TokenizingListHandler(RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def get(self):
        self.post()

    def post(self):
        text = self.get_argument('text',default="").strip()
        language = self.get_argument('language',default="en").strip()
        if len(text) == 0:
            result = {"success":False,"message":"Please input the text!"}
        else:
            if language not in list_language_supported:
                result = {"success":False,"message":"This language is not supported"}
            else:
                result = {"success":True, "input":{"text": text, "language": language}, "output": tokenize(text, language)}
        self.write(json.dumps(result))

class TokenizingStringHandler(RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def get(self):
        self.post()

    def post(self):
        text = self.get_argument('text',default="").strip()
        language = self.get_argument('language',default="en").strip()
        if len(text) == 0:
            result = {"success":False,"message":"Please input the text!"}
        else:
            if language not in list_language_supported:
                result = {"success":False,"message":"This language is not supported"}
            else:
                result = {"success":True, "input":{"text": text, "language": language}, "output": tokenize_join(text, language)}
        self.write(json.dumps(result))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/tokenize", TokenizingListHandler),
        (r"/tokenize_join",TokenizingStringHandler),
    ])

def main(argv):
    try:
        port_num = int(args.p)
    except:
        port_num = 3000

    try:
        n_process = int(args.n)
    except:
        n_process = 1
        
    app = make_app()

    server = httpserver.HTTPServer(app)
    server.bind(port_num)
    server.start(n_process)  

    link_list = "http://0.0.0.0:" + str(port_num) + "/tokenize"
    link_string = "http://0.0.0.0:" + str(port_num) + "/tokenize_join"
    print ("* Tokenize to list: Running on " + link_list + ", waiting for requests only (Press Ctrl+C to stop)")
    print ("* Tokenize to string: Running on " + link_string + ", waiting for requests only (Press Ctrl+C to stop)")

    IOLoop.current().start()

if __name__ == '__main__':
    main(sys.argv)