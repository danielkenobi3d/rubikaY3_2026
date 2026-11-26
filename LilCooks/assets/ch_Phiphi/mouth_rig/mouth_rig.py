from RMPY.rig.biped.rig import arm
from rubikaY3_2026.Professor.assets.happy.arm_rig import attachToGeo
from RMPY.rig import rigOutput
import maya.mel as mel
from builder.pipeline import environment
from RMPY.core import data_save_load
from RMPY.creators import shrinkWrap

def build():
    rig_output = rigOutput.RigOutput()

    arm_points = ['C_mouth00_reference_pnt']
    new_arm = arm.Arm()
    new_arm.create_point_base(*arm_points)

    shoulder_attach = attachToGeo.AttachToGeo()
    shoulder_attach.create_point_base(arm_points[0], geometry='C_head00_msh')

    new_arm.set_parent(shoulder_attach, create_hierarchy_joints=True, output_joint_rig = rig_output)

    env = environment.Environment()
    data_save_load.load_skin_cluster('C_mouth_msh')

    shrink_wrap = shrinkWrap.ShrinkWrap()
    shrink_wrap.geo_base('C_mouth_msh', target = 'C_head00_msh')
    #shrink_wrap.load('C_mouth_msh_shw')

    # pm.select('R_arm_body_msh', 'C_head00_body_msh')
    # mel.eval('CreateShrinkWrap;')

def save_data():
    shrink_wrap = shrinkWrap.ShrinkWrap.by_node('C_mouth_msh')
    shrink_wrap.save()


if __name__=='__main__':
    build()




