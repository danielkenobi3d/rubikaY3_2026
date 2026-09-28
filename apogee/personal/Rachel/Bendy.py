import pymel.core as pm


def curve_by_points(*points):
    point_data = []
    # print (points, points.__class__)
    for each in points :
        print (each.translate.get())
    print (point_data)
    point_data = [each.translate.get() for each in points] #in one ligne
    new_Curve = pm.curve(editPoint =point_data)
    pm.rebuildCurve(new_Curve, rebuildType = 0, keepRange= 0, constructionHistory = True, replaceOriginal = False)


selection = pm.ls(selection=True)
#print(selection, selection.__class__)
curve_by_points(*selection)