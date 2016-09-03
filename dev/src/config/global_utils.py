# -*- coding: utf-8 -*-


def convert_to_builtin_type(obj): 
    #print 'default(', repr(obj), ')' # 把Obj对象转换成dict类型的对象
    d = {  }
    d.update(obj.__dict__)
    return d
    
