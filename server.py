#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

data = json.load(open('questions.json'))

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        text = self.get_question_text(data[0])
        
        self.wfile.write("<html><body>" + text + "</body></html>")
   
    def click():
        entered_text = entry.get()

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

    def get_question_text(self, question):
        text = "<h2>" + question["text"] + "</h2>"
        # iterate data[0].choices
        text = text + "<select>"
        for idx, val in enumerate(question["choices"]):
            text = text + "<option value='" + val["text"] + "'>" + val["text"] + "</option>"
            #print(idx, val)

        return text + "</select>"

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

def get_quiz(data, idx):
  val = data[idx]
  print("please select one of the options below and answer questions as accurately as possible to ensure the best results")
  #print(data[0])

  #text = get_question_text(data[0])

  #menu=input(text)

  #print(menu)

  # based on menu get the id from data[0]["choices"]

  selId = ""
  # print the next relevant question
  # iterate over data but skip index 0 and then look for id from choice
  #if idx > 0 and val["type"] != selId:
  #  continue

  text = get_question_text(data[idx])

  if idx == 0:
    selId = val["choices"][menu-1]["id"]  
    print("You selected:" + selId)

    # validate menu