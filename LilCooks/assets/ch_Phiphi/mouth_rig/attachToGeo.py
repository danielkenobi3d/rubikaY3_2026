from RMPY.rig import rigBase
from RMPY.rig import rigUVPin
import pymel.core as pm
class AttachToGeoModel(rigBase.BaseModel):
    def __init__(self):
        super(AttachToGeoModel, self).__init__()
        self.geometry = None
        self.uv_pin_attach = None
        self.uv_pin_surface_constrained = None


class AttachToGeo(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        kwargs['model'] = kwargs.pop('model', AttachToGeoModel())
        super(AttachToGeo, self).__init__(*args, **kwargs)

    def create_point_base(self, *args, **kwargs):
        super(AttachToGeo, self).create_point_base(*args, **kwargs)
        self.geometry = pm.ls(kwargs.pop('geometry', None))

        self.uv_pin_attach = rigUVPin.RigUVPin()# rig_system=self.rig_system
        self.uv_pin_surface_constrained = rigUVPin.RigUVPin()
        reset_control, control = self.create.controls.point_base(*args, size=.1)
        pm.parent(reset_control, self.rig_system.controls)
        self.controls.append(control)
        self.reset_controls.append(reset_control)
        self.uv_pin_attach.create_point_base(reset_control, geometry=self.geometry)
        self.uv_pin_surface_constrained.create_point_base(reset_control, geometry=self.geometry)
        self.create.constraint.matrix_node_base(self.uv_pin_attach.tip, reset_control)
        self.uv_pin_attach.clean_up()
        self.create.constraint.matrix_node_base(control, self.uv_pin_surface_constrained.position_reference_locator, mo=True)
        self.tip = self.uv_pin_surface_constrained.tip



if __name__ == '__main__':
    print('whatever')
    my_rig = AttachToGeo()
    my_rig.create_point_base(*pm.ls('C_mouth00_reference_pnt'), geometry='C_head00_msh')