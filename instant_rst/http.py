#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import os.path
import urllib,urllib2

def get(url, headers={}):
    req = urllib2.Request(
        url = url,
        headers = headers
    )
    f = urllib2.urlopen(req)
    con = f.read()
    return {'code':f.getcode(), 'content':con}

def post(url, data, headers={}):
    req = urllib2.Request(
        url = url,
        headers = headers
    )
    f = urllib2.urlopen(req, urllib.urlencode(data))
    con = f.read()
    return {'code':f.getcode(), 'content':con}

def main(args=sys.argv[1:]):
    url = args[0]

    filename = os.path.abspath(args[1])

    if len(args) >= 3 :
        p = args[2]
    else:
        p = -1
    print post(url, {'file':filename, 'p':p})
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
