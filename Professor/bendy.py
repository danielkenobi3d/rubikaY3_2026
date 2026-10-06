import pymel.core as pm

offset = [1, 0, 0,  0,
          0, 1 , 0, 0,
          0, 0, 1 , 0,
          0, 3, 0 , 1]


def offset_point(scene_node, offset_value):
    """
    This function creates a locator that will follow the scene Node with and offset value defined by offset_value
    """
    mult_matrix = pm.createNode('multMatrix')
    # pm.connectAttr(f'{scene_node}.wordMatrix[0]', f'{mult_matrix}.matrixIn[0]')
    # pm.connectAttr(scene_node.wordMatrix[0], mult_matrix.matrixIn[0])
    mult_matrix.matrixIn[0].set(offset_value)
    scene_node.worldMatrix[0] >> mult_matrix.matrixIn[1]
    space_loc = pm.spaceLocator()
    mult_matrix.matrixSum >> space_loc.offsetParentMatrix

scene_node = pm.ls('locator1')[0]
offset_point(scene_node, offset)



def curve_by_points(*points):
    point_data = []
    for each in points:
        point_data.append(each.translate.get())

    new_curve = pm.curve(point = point_data)

    for index, each in enumerate(points):
        each.worldPosition[0] >> new_curve.controlPoints[index]




selection = pm.ls(selection=True)

curve_by_points(*selection)

import maya.cmds as cmds
pm.connectAttr('locatorShape5.worldPosition[0]', 'curveShape1.controlPoints[0]')