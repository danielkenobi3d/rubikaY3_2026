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
    """
    Creates a curve on the provided points and connects the world position of the locators to the curve
    :param points:
    :return:
    """
    point_data = []
    for each in points:
        point_data.append(each.translate.get())

    new_curve = pm.curve(point = point_data)

    for index, each in enumerate(points):
        each.worldPosition[0] >> new_curve.controlPoints[index]


selection = pm.ls(selection=True)

curve_by_points(*selection)

def create_joints_on_curve(curve, number_of_joints):
    joints_group = pm.group(empty=True, name= 'joints_group')
    length_of_curve = curve.numSpans()

    step = length_of_curve/(number_of_joints-1)
    for index in range(number_of_joints):
        pm.select(clear=True)
        new_joint = pm.joint()
        new_joint.setParent(joints_group)

        my_path = pm.ls(pm.pathAnimation(new_joint, curve=curve))[0]
        pm.delete(pm.listConnections(my_path.uValue))
        my_path.uValue.set(step*index)




