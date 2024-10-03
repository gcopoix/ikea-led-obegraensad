Import("env")
import os
import time, datetime


# make sure destination file webgui.cpp exists for platformio build
dst = 'src/webgui.cpp'
if not os.path.isfile(dst):
    open(dst, 'a').close()
    os.utime(dst, (0, 0))

def build_webgui(env, node):
    # check if any of the src files in frontend folders is newer than the dst file
    src_dirs = [ 'frontend/dist', 'frontend/src', 'frontend' ]
    src_files = []
    dst_time = os.path.getmtime(dst)
    for d in src_dirs:
        src_files += [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and not f.endswith('-lock.json')]
    for f in src_files:
        if os.path.getmtime(f) > dst_time:
            # some frontend file has been updated -> need webgui.cpp rebuild
            env.Execute('cd frontend; npm config set fund false; npm i; npm run build')
            break
    return node

# add extra build step to generate webgui.cpp
env.AddBuildMiddleware(build_webgui, '*/'+dst)
