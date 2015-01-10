#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
''' Simply open browser 1 seconds after start server,
    As we don't want to use hooking
    which need rewrite HttpServer.run() '''
import os
import sys
import time
import webbrowser

from multiprocessing import Process

from instant_rst import args
from instant_rst.http import post
from instant_rst.server import run

import socket


# get hostname of local LAN IP
HOST = socket.gethostbyname(socket.gethostname())

def browse(b, port, filename):
    time.sleep(3)
    url =  'http://' + HOST + ':'+ port
    webbrowser.open(url)
    time.sleep(3)
    post(url, {'file': filename})

def main():
    ag = args.parse()

    p = Process(target=browse, args=(ag.browser, ag.port, ag.filename))
    p.start()

    try:
        run(host=HOST, port=int(ag.port),
            template_dir=ag.template_dir,
            static_dir=ag.static_dir)
    except:
        print '\nSome error/exception occurred.'
        print sys.exc_info()
        p.terminate()
        sys.exit()

if __name__ == "__main__":
    main()
