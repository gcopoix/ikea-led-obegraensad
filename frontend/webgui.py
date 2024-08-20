Import("env")
import os

dst = 'src/webgui.cpp'

# make sure webgui.cpp exists for platformio build
if not os.path.isfile(dst):
    open(dst, 'a').close()

def build_webgui(env, node):
    env.Execute('cd frontend; npm config set fund false; npm i; npm run build')
    return node

# add extra build step to generate webgui.cpp
env.AddBuildMiddleware(build_webgui, '*/'+dst)
