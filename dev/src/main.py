# -*- coding: utf-8 -*-


from config import *


def run_callback(socket):
    render._keywords['globals']=global_vars
    render._keywords['globals']['render']=render
    

if __name__ == "__main__":
    
    urls=load_all_urls()
    start(urls, run_callback=run_callback)

    
    