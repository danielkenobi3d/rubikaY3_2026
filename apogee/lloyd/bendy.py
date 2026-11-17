import pymel.core as pm

offset = [1, 0, 0, 0,
          0, 1, 0, 0,
          0, 0, 1, 0,
          0, 3, 0, 0,]

def offset_point(scene_node: {createNode, wordMatrix, spaceLocator}, offset_value: {createNode, spaceLocator}):
    mult_matrix = pm.createNode('multMatrix')

    # pm.connectAttr(f'{scene_mode}.wordMatrix[0]', f'

