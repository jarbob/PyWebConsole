# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:59:26 2015

@author: java
"""


from config import *


class index():
   
    
    def GET(self):
        
        
        #print super(self)
        #print type(getdata("superman"))
        
        setdata=getdata("set")
        if setdata:
            print "set session"
            setcookie('age', setdata, 3600)
        
        
        foo = cookies()
        print "test cookie:", foo
        try:
            print foo.age
        except:
            print "None"
        
        
        return render.home.index()
        pass
    
