import pymel.core as pm


def curve_by_points(*points):
    point_data = []
    for each in points:
        point_data.append(each.translate.get())
    # point_data =[each.translate.get() for each in points]
    new_curve = pm.curve(editPoint=point_data)
    pm.rebuildCurve(new_curve,
                    rebuildType=0,
                    keepRange = 0,
                    replaceOriginal=False,
                    constructionHistory = True)



selection = pm.ls(selection=True)

curve_by_points(*selection)

import maya.cmds as cmds
pm.connectAttr('locatorShape5.worldPosition[0]', 'curveShape1.controlPoints[0]')