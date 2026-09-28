import pymel.core as pm
import maya.cmds as cmds


GapCount = 0
nbrJ = 5
Jump = 2

existing_joints = cmds.ls('joint*', type='joint')
if existing_joints:
    cmds.delete(existing_joints)

for each in range(nbrJ):
    Lejoint = cmds.createNode('joint')
    my_path = cmds.pathAnimation(Lejoint, curve='curve1')
    Space = cmds.createNode('floatConstant')
    cmds.setAttr(f'{Space}.inFloat', GapCount)
    GapCount += Jump

    source_conn = cmds.listConnections(f'{my_path}.uValue', plugs=True)
    if source_conn:
        cmds.disconnectAttr(source_conn[0], f'{my_path}.uValue')
    cmds.connectAttr(f'{Space}.outFloat', f'{my_path}.uValue')
