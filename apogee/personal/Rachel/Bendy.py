import pymel.core as pm


def curve_by_points(*points):
    # print (points, points.__class__)
    for each in points :
        print (each)


selection = pm.ls(selection=True)
#print(selection, selection.__class__)
curve_by_points(*selection)