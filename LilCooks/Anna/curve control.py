import pymel.core as pm


def curve_by_points(*points):
    point_data = []
    for each in points:
        point_data.append(each.translate.get())
    print(point_data)
    new_curve = pm.curve(point=point_data)
    pm.rebuildCurve(new_curve, rebuildType=0, keepRange=0, replaceOriginal=True, constructionHistory=True,
                    keepControlPoints=True)


n = 4
selection = pm.ls(selection=True)

curve_by_points(selection)

for x in range(n):
    pm.connectAttr(f'locatorShape{x + 1}.worldPosition[0]', f'curveShape1.controlPoints[{x}]')

for i in range(n):
    pm.circle()[0].setTranslation(pm.PyNode(f'locator{i + 1}').getTranslation(worldSpace=True), worldSpace=True)

for i in range(n):
    pm.parent(f'locatorShape{i + 1}', f'nurbsCircleShape{i + 1}')