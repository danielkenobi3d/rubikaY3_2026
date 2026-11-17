import pymel.core as pm

offset = [1,0,0,0,
          0,0,0,0,
          3,0,0,0,]

def prout(*points):
    for each in points
def offset_point (scene_node, offset_value)
    mult_matrix = pm.createNode('mult_matrix')

    # pm. connectAttr (f'(scene node).wordMatrix[0]', f'(mult matrix).matrixin(0]')
    # pm. connectAttr (scene node.wordMatrix[0]. mult_matrix.matrixIn[0])
    mult_matrix.matrixIn[0].set (offset_value)
    scene_node.worldMatrix[0] >> mult_matrix.matrixIn[1]
    space_loc = pm.spacelocator()
    mult_matrix.matrixSun >> space_loc.offsetParentMatrix

selection = pm.ls(selection=True)
prout(*selection) No newline at end of file
    scene_node=(pm.lslocator1) No newline at end of file