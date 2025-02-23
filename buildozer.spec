[app]
title = Steam Spray Calculator
package.name = steamapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv
version = 1.0
requirements = python3,kivy,pyXSteam
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 20
android.ndk = 23b

[buildozer]
log_level = 2
warn_on_root = 1