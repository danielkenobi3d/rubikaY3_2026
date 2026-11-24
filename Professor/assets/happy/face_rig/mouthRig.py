from rubikaY3_2026.Professor.assets.happy.face_rig import pinPoints
from rubikaY3_2026.Professor.assets.happy.face_rig import rigCurveMouth
import importlib
import pymel.core as pm
importlib.reload(rigCurveMouth)
importlib.reload(pinPoints)

from RMPY.rig import rigBase


class RigMouthModel(rigBase.BaseModel):
    def __init__(self):
        super(RigMouthModel, self).__init__()
        self.rig_curve=None
        self.rig_points = None
        self.geometry = None


class RigMouth(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        kwargs['model'] = kwargs.pop('model', RigMouthModel())
        super(RigMouth, self).__init__(*args, **kwargs)
        
    def create_point_base(self, *args, **kwargs):
        super().create_point_base(*args, **kwargs)
        self.geometry = pm.ls(kwargs.pop('geometry', None))

        self.rig_curve = rigCurveMouth.RigCurveMouth()
        self.rig_curve.create_point_base(*args, **kwargs)
        self.rig_points = pinPoints.PinPoints()
        self.rig_points.create_point_base(*self.rig_curve.reset_controls, geometry=self.geometry)

        for reset_control, uv_pin_locator in zip(self.rig_curve.reset_controls, self.rig_points.outputs):
            self.create.constraint.matrix_node_base(uv_pin_locator, reset_control, mo=True)


if __name__ == '__main__':
    list_of_points = pm.ls('C_mouth00_reference_pnt', 'C_mouth01_reference_pnt', 'C_mouth02_reference_pnt',
                           'C_mouth03_reference_pnt', 'C_mouth04_reference_pnt', 'C_mouth05_reference_pnt')
    my_rig = RigMouth()
    my_rig.create_point_base(*list_of_points,  geometry='pSphere1')