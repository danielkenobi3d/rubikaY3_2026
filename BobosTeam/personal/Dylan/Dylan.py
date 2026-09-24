import pymel.core as pm


def curve_by_points(*points):
    for each in points:
        print(each)


    selection = pm. ls(selection=True)

    curve_by_points(*selection)