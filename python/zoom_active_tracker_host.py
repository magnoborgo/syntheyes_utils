# this script will zoom on the active tracker host path (camera/objects)
# by Magno Borgo 2022

import sys
PY3 = sys.version_info[0] == 3

if PY3:
    import SyPy3 as sypy
else:
    import SyPy as sypy

hlev = sypy.SyLevel()
hlev.OpenExisting()
hlev.SetView("Quad")

cam = hlev.Scene().activeObj

views = ["top","front","left"]

hlev.Begin() #begin undo action

visibleObjList = []

for o in hlev.Objects():
    if o.show == 1.0 and o != cam:
        o.Set("show",0.0)
        visibleObjList.append(o)

for t in hlev.Trackers():
    if t.Get("isShown"):
        t.Set("isShown",0.0)
        visibleObjList.append(t)
        # print(t)
for m in hlev.Meshes():
    if m.show == 1.0:
        m.Set("show",0.0)
        visibleObjList.append(m)

hlev.Accept("Hide all visible scene objects except the camera")

for v in views:
    vp = hlev.Main().ByName(v)
    vp.PerformActionByNameAndWait("3D/Zoom to Fill")

hlev.Begin()
for t in visibleObjList:

    if t.Type() in ["TRK"]:
        t.Set("isShown",1.0)
    else:
        t.Set("show",1)
        print(t.nm, t.Type(),t.show)
hlev.Accept("Show all previous visible scene objects")