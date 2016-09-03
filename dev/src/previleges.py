# -*- coding: utf-8 -*-

from config import *
import json



#判断读写权限

class user_rights(have_system_rights):
    
    
    
    def have_prevelegies(self):
        import login
        self.fail_class=login.login()

        user_id=cookie('user_id')
        if debug:
            print "user_rights:user_id:",user_id

        return user_id
        
       
       
"""
class user_rights_read(have_system_rights_read):
    fail_url="/login"
    
    def have_prevelegies(self):
       
       user_id=cookie('user_id')
       
       return user_id

       
       
class user_rights_write(have_system_rights_write):
    fail_url="/login"
    
    def have_prevelegies(self):
       
       user_id=cookie('user_id')
       
       return user_id
"""
 
 
 
 
 
 
 
 
 