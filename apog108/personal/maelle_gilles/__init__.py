import maya.cmds as pm


def curve_by_point(*points):
    point_data = []
    for each in points:
        point_data.append(each.translate.get())

    # point_data =[each.translate.get() for each in points]
    print(point_data)
    pm.curve (point=point_data)



selection = pm.ls(selection=True)

curve_by_points(*selection)