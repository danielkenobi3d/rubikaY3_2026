import maya.cmds as cmds
import pymel.core as pm


def curve_by_pts(*pts):
    pts_data = []

    print(pts)
    for each in pts:
        pts_data.append(each.translate.get())
    my_Curve = pm.curve(p=pts_data)
    pm.rebuildCurve(my_Curve, rebuildType=0, keepRange=0, replaceOriginal=False, constructionHistory=True, keepControlPoints=True)

    n = 0

    for each in pts:
        my_locShape = each.getShape()
        print(each)
        pm.connectAttr(f'{my_locShape}.worldPosition[0]', f'{my_Curve}.controlPoints[{n}]')

        new_circle = pm.circle()
        pm.matchTransform(new_circle, each, pos=True, rot=False)
        pm.parent(f'locatorShape{n + 1}', f'nurbsCircleShape{n + 1}')

        n = n + 1


selection = pm.ls(selection=True)
curve_by_pts(*selection)