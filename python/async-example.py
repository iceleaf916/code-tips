#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt
import functools
import threading
import time

def async(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper

start = time.time()
cache = apt.Cache()
print time.time() - start
cache.update()
print time.time() - start

@async
def update_cache():
    cache = apt.Cache()
    cache.update()

print time.time() - start
