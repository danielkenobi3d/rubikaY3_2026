from RMPY.rig import rigFromHierarchy
import pymel.core as pm
from RMPY.rig import rigWorld

def build_rig():
    my_rig = rigFromHierarchy.RigFromHierarchy()
    my_rig.create_point_base(*pm.ls('C_COG00_reference_pnt'))
    world_rig = rigWorld.RigWorld()
    my_rig.set_parent(world_rig)
