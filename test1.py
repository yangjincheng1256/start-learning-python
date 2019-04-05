# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:04:48 2019

@author: hbsdg
"""

mo=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",
    91,["Graham Chapman",["Michael Palin","John Cleese",
            "Terry Gilliam","Eric Idle","Terry Jones"]]]
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(mo)