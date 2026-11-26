from RMPY.rig import rigBase
from RMPY.rig import rigUVPin
import pymel.core as pm

class PinPointsModel(rigBase.BaseModel):
    def __init__(self):
        super(PinPointsModel, self).__init__()
        self.geometry = 'pCube1'
        self.outPositionPoints = []
        self.uv_pins_attach_controls = []
        self.uv_pins_driving_outputs = []


class PinPoints(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        kwargs['model'] = kwargs.pop('model', PinPointsModel())
        super(PinPoints, self).__init__(*args, **kwargs)

    @property
    def outputs(self):
        return [each.tip for each in self.uv_pins_driving_outputs]

    def create_point_base(self, *points, **kwargs):
        super(PinPoints, self).create_point_base(*points, **kwargs)
        self.geometry = pm.ls(kwargs.pop('geometry', None))
        if self.geometry:
            for each_point in points:
                reset_control, control = self.create.controls.point_base(each_point, size=.1)
                self.controls.append(control)
                self.reset_controls.append(reset_control)

                pm.parent(reset_control, self.rig_system.controls) # this is the rig hierarchy
                if self.uv_pins_driving_outputs:
                    uv_pins_attach_controls = rigUVPin.RigUVPin(rig_system= self.uv_pins_driving_outputs[0].rig_system)
                    uv_pins_driving_outputs = rigUVPin.RigUVPin(rig_system=self.uv_pins_attach_controls[0].rig_system)
                else:
                    uv_pins_attach_controls = rigUVPin.RigUVPin()
                    uv_pins_driving_outputs = rigUVPin.RigUVPin()

                self.uv_pins_attach_controls.append(uv_pins_attach_controls)
                self.uv_pins_driving_outputs.append(uv_pins_driving_outputs)
                uv_pins_attach_controls.create_point_base(control , geometry=self.geometry,
                                                          system='drivingControls')
                uv_pins_attach_controls.clean_up()
                self.create.constraint.matrix_node_base(uv_pins_attach_controls.tip, reset_control, mo=True)
                uv_pins_driving_outputs.create_point_base(control, geometry =   self.geometry,
                                                          system='outputsControls')
                self.create.constraint.matrix_node_base(control, uv_pins_driving_outputs.position_reference_locator, mo=True)

if __name__ == '__main__':
    list_of_points = pm.ls('C_mouth00_reference_pnt', 'C_mouth01_reference_pnt', 'C_mouth02_reference_pnt', 'C_mouth03_reference_pnt', 'C_mouth04_reference_pnt', 'C_mouth05_reference_pnt')
    attach_points = PinPoints()
    attach_points.create_point_base(*list_of_points, geometry='pSphere1')