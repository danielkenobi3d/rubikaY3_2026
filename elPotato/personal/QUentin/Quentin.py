import maya.cmds as cmds
import pymel.core as pm


def motion(nb_jnt):
    my_ctrl = 'ctrl'

    if nb_jnt == 0:
        print('the function cant work without anny joints selected')

    else:
        i = 0
        mul = 2

        while i < nb_jnt:

            #               my_joint = cmds.createNode('joint')
            #                cmds.pathAnimation( my_joint, c='curve1', stu=0, etu=1, follow=True)

            #               path_animation = cmds.listHistory(my_joint, "motionPath"+str(i+1))
            #                cmds.delete(path_animation[3])
            ## to creat a joint and get the name of the u

            if i == 0:

                my_joint = cmds.createNode('joint')
                cmds.pathAnimation(my_joint, c='curve1', stu=0, etu=1, follow=True)

                path_animation = cmds.listHistory(my_joint, "motionPath" + str(i + 1))
                cmds.delete(path_animation[3])

                cmds.connectAttr(f'{my_ctrl}.path', f'{path_animation[2]}.uValue')

                i += 1

            elif i == 1:

                my_joint = cmds.createNode('joint')
                cmds.pathAnimation(my_joint, c='curve1', stu=0, etu=1, follow=True)

                path_animation = cmds.listHistory(my_joint, "motionPath" + str(i + 1))
                cmds.delete(path_animation[3])

                my_sum = cmds.createNode('sum')

                cmds.connectAttr(f'{my_ctrl}.path', f'{my_sum}.input[0]')
                cmds.connectAttr(f'{my_ctrl}.offset', f'{my_sum}.input[1]')
                cmds.connectAttr(f'{my_sum}.output', f'{path_animation[2]}.uValue')

                i += 1

            else:
                print('yes')

                my_joint = cmds.createNode('joint')
                cmds.pathAnimation(my_joint, c='curve1', stu=0, etu=1, follow=True)

                path_animation = cmds.listHistory(my_joint, "motionPath" + str(i + 1))
                cmds.delete(path_animation[3])

                my_float = cmds.createNode('floatConstant')
                cmds.setAttr(f"{my_float}.inFloat", mul)

                my_multy = cmds.createNode('multiply')

                my_sum = cmds.createNode('sum')

                cmds.connectAttr(f'{my_float}.outFloat', f'{my_multy}.input[0]')
                cmds.connectAttr(f'{my_ctrl}.offset', f'{my_multy}.input[1]')

                cmds.connectAttr(f'{my_ctrl}.path', f'{my_sum}.input[0]')
                cmds.connectAttr(f'{my_multy}.output', f'{my_sum}.input[1]')
                cmds.connectAttr(f'{my_sum}.output', f'{path_animation[2]}.uValue')

                mul += 1

                i += 1


motion(10)