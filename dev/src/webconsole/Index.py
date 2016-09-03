# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:59:26 2015

@author: java
"""

from config import *
import webconsole


class html():
    def GET(self, message=None):
        action = getdata('action')
        if 'get' == action:
            if webconsole.output_queue.qsize() > 0:

                return webconsole.output_queue.get()
            else:
                return 0
        return render.webconsole.index()

    def POST(self):

        data = getdata(None)  # 获取所有的数据
        if data:

            webconsole.input_queue.put(data)
            webconsole.CommandHandle()



        # todo-me finish the template
