# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:59:26 2015

@author: java
"""


from config import *


class index():
   
    
    def GET(self, message=None):
        
        
        
        return render.upload.index(message)
        
        
    def POST(self):
        
        data=getdata(None)                          #获取所有的数据

        if data and data.get('myfile', None):
             
            upload=save_upload_file("upload/", "myfile")
            
            #为了保证解码统用＋来拼写
            upload="<h2><font color=green>上传成功："+upload +"</font>"
            return self.GET(upload)
            
        return "### Error #1: no data"