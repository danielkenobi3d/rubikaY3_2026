import maya.cmds as cmds
x=0
curve_name = cmds.curve(
        degree=3,
        point=[(0, 0, 0), (5, 0, 5), (15, 3, 5), (25, -3, -5), (35, 0, 0)],
        knot=[0, 0, 0, 1, 2, 2, 2],
    )
for each in range(10):

    my_joint = cmds.createNode('joint')
    constraint = cmds.pathAnimation(my_joint,curve_name)
    my_float = cmds.createNode('floatConstant')
    #print{my_float}.outFloat'}
    cmds.setAttr(f'{my_float}.inFloat',x)
    x+=0.3
    Connect=cmds.listConnections (f'{constraint}.uValue',plugs=True)
    cmds.disconnectAttr(Connect[0],f'{constraint}.uValue')
    cmds.connectAttr(f'{my_float}.outFloat', f'{constraint}.uValue')

print (my_joint)