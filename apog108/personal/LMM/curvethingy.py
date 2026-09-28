import pymel.core as pm
import maya.cmds as cmds


def curve_by_points(*points):
    point_data = []
    for each in points:
        point_data.append(each.translate.get())
        pm.curve(point=point_data)

    print(points[0])
    print(points, points._class_)


selection = pm.ls(selection=True)
print(selection, slection._class_)

curve_by_point(*selection)

import pymel.core as pm
import maya.cmds as cmds


def curve_by_points(*points):
    point_data = []
    for each in points:
        point_data.append(each.translate.get())
    new_curve = pm.curve(point=point_data)
    pm.rebuildCurve(new_curve, rebuildType=0, keepRange=0)


selection = pm.ls(selection=True)
curve_by_points(*selection)