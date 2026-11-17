from RMPY.rig import rigFromHierarchy
import pymel.core as pm


def build_rig():
    my_rig = rigFromHierarchy.RigFromHierarchy()
    my_rig.create_point_base(*pm.ls('C_COG00_reference_pnt'))