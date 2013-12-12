"""
have fun maniac
"""

def methoverload(obj,name,func):
    old=obj.__getattribute__(name)
    obj.__setattr__(name,type(old)(func,obj))
    return old

def overload(obj,**methods):
    old = {}
    for m in methods:
        old[m] = methoverload(obj,m,methods[m])
    return old
