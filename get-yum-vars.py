#!/usr/bin/python
import yum, json

base = yum.YumBase()
base.preconf.debuglevel = 0
base.preconf.errorlevel = 0
vars = base.conf.yumvar

print(json.dumps(vars, indent=2))
