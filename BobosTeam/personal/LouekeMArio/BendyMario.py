import pymel.core as pm


def curve_by_points(*points):
    point_data=[]
    for each in points:
        point_data.append(each.translate.get())
        print(each.translate.get())

        #point_data=[each.translate.get() for each in points]
    new_curve= pm.curve(point=point_data)
    pm.rebuildCurve(new_curve,
                    rebuildType=0,
                    keepRange=0,
                    replaceOriginal=True,
                    constructionHistory=False,)


selection = pm.ls(selection=True)


curve_by_points(*selection)