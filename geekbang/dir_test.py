#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from pathlib import Path

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.exists('/Users'))
print(os.path.isfile('/Users'))
print(os.path.isdir('/Users'))
print(os.path.join('/Users', 'github'))

p = Path('.')
print(p.resolve())
print([x for x in p.iterdir() if x.is_dir() ])

print(p.is_dir())
