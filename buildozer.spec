[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
android.permissions = INTERNET
android.api = 28
android.minapi = 21
android.ndk = 23b
p4a.branch = master

[loggers]
keys = root

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = console

[handler_console]
class = StreamHandler
args = (sys.stdout,)
level = INFO
formatter = generic

[formatter_generic]
format = %(levelname)s: %(message)s
