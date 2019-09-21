#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

import hmac
message = b'Hello, world!'
key = b'secret'

h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())