import maya.cmds as cmds
import pymel.core as pm


def curve_by_pts(*pts):
    pts_data = []
    print(pts)
    for each in pts:
        pts_data.append(each.translate.get())
    # egale en haut pts_data= [each.translate.get() for each in pts]

    pm.curve(point=pts_data)
    #pm.curve(editPoint=pts_data) --> to force them to go on the points


selection = pm.ls(selection=True)
# points needs to be selected in the correct order, from the first one on the ligne to the last

curve_by_pts(*selection)

#---------------------------------------------------------------------------------------
import maya.cmds as cmds
import pymel.core as pm

def curve_by_pts02(*pts):
    pts_data = []
    print(pts)
    for each in pts:
        pts_data.append(each.translate.get())

    new_curve = pm.curve(editPoint=pts_data)
    pm.rebuildCurve(new_curve, rebuildType= 0, keepRange=0, replaceOriginal = False, constructionHistory =True)

selection = pm.ls(selection=True)

curve_by_pts(*selection)