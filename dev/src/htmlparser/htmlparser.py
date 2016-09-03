# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:14:37 2016

@author: dev
"""

from config import *

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    result={}
    
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

        return
        
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        self.result[self.lasttag]=data
        print "Encountered some data  :", data



def alanysis_html(src):
    # instantiate the parser and fed it some HTML
    
    parser = MyHTMLParser()
    parser.feed(src)
    return parser.result




class index():
    
    def GET(self):
        alanysis=None
        
        
        postdata="" #search=1&status=2
        url=getdata("url")

        print "url:", url
        
        status, output=read_url(url, postdata)
        print "status:", status, "output:", output
        

        if status == 0:
            alanysis=alanysis_html(output)
        
        if not url:
            url="http://www.baidu.com/"
            
        return render.htmlparser.index(url, alanysis, output)
    
    def POST(self):
        return self.GET()
        
        