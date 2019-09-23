#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

import struct
print(struct.pack('>I', 10240099))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))