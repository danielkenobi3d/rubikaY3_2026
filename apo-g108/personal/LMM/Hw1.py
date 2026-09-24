import pymel.core as pm
import maya.cmds as cmds
import random

sl = 0
off = 5
x = sl

for each in range (10):
    y=cmds.createNode ('joint')
    z=cmds.pathAnimation (y,curve='curve1')
    Connect=cmds.listConnections (f'{z}.uValue',plugs=True)
    if Connect:
        cmds.disconnectAttr(Connect[0],f'{z}.uValue')
    w=cmds.createNode ('floatConstant')
    cmds.setAttr(f'{w}.inFloat',x)
    cmds.connectAttr(f'{w}.outFloat',f'{z}.uValue')
    x+=off