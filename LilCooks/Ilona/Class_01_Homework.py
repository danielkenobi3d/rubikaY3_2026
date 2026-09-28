import maya.cmds as cmds

my_circle = cmds.circle()[0]
cmds.addAttr(my_circle, longName='Path', attributeType='float')
cmds.setAttr(f'{my_circle}.Path', 5, keyable=True)

cmds.addAttr(my_circle, longName='OffSet', attributeType='float')
cmds.setAttr(f'{my_circle}.OffSet', 1, keyable=True)

cmds.select(clear=True)

nb_joints = 10
for n1 in range(nb_joints):
    my_joint = cmds.joint()
    my_path = cmds.pathAnimation(my_joint, curve='curve2')
    cmds.delete(f'{my_path}_uValue')

    my_sum = cmds.createNode("sum")
    my_float = cmds.createNode("floatConstant")

    cmds.connectAttr(f'{my_circle}.Path', f'{my_sum}.input[0]')
    cmds.connectAttr(f'{my_sum}.output', f'{my_path}.uValue')
    cmds.connectAttr(f'{my_circle}.OffSet', f'{my_float}.inFloat')

    for n2 in range(n1 + 1):
        cmds.connectAttr(f'{my_float}.outFloat', f'{my_sum}.input[{n2 + 1}]')

