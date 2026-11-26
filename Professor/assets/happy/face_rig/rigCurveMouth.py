from RMPY.rig import rigBase
import pymel.core as pm

class RigCurveMouthModel(rigBase.BaseModel):
    def __init__(self):
        super(RigCurveMouthModel, self).__init__()
        self.curve = None


class RigCurveMouth(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        kwargs['model'] = kwargs.pop('model', RigCurveMouthModel())
        super(RigCurveMouth, self).__init__(*args, **kwargs)
    
    def create_point_base(self, *points, **kwargs):
        super(RigCurveMouth, self).create_point_base(*points, **kwargs)
        self.curve = self.create.curve.point_base(*points)
        direct_indices = [0, 2, 3, 5]
        for index in direct_indices:
            reset_control, control = self.create.controls.point_base(points[index], size=.05)
            pm.parent(reset_control, self.rig_system.controls)  # this is the rig hierarchy
            self.reset_controls.append(reset_control)
            self.controls.append(control)
    
        for control, index in zip(self.controls, direct_indices):
            print('control index:', control, index)
            decompose_matrix = pm.createNode('decomposeMatrix')
            control.worldMatrix[0] >> decompose_matrix.inputMatrix
            decompose_matrix.outputTranslate >> self.curve.controlPoints[index]
            self.name_convention.rename_name_in_format(decompose_matrix, name='controlCurve')


        offset_matrix = points[1].worldMatrix[0].get() * points[0].worldMatrix[0].get().inverse()

        multiply_matrix = pm.createNode('multMatrix')
        decompose_matrix = pm.createNode('decomposeMatrix')
        self.name_convention.rename_name_in_format(multiply_matrix, decompose_matrix, name='secondVtx')
        multiply_matrix.matrixIn[0].set(offset_matrix)
        self.controls[0].worldMatrix[0] >> multiply_matrix.matrixIn[1]
        multiply_matrix.matrixSum >> decompose_matrix.inputMatrix
        decompose_matrix.outputTranslate >> self.curve.controlPoints[1]

        offset_matrix = points[4].worldMatrix[0].get() * points[5].worldMatrix[0].get().inverse()

        multiply_matrix = pm.createNode('multMatrix')
        decompose_matrix = pm.createNode('decomposeMatrix')
        self.name_convention.rename_name_in_format(multiply_matrix, decompose_matrix, name='fifthVtx')
        multiply_matrix.matrixIn[0].set(offset_matrix)
        self.controls[3].worldMatrix[0] >> multiply_matrix.matrixIn[1]
        multiply_matrix.matrixSum >> decompose_matrix.inputMatrix
        decompose_matrix.outputTranslate >> self.curve.controlPoints[4]









if __name__ == '__main__':
    reference_points = pm.ls('C_mouth00_reference_pnt', 'C_mouth01_reference_pnt',
            'C_mouth02_reference_pnt', 'C_mouth03_reference_pnt', 'C_mouth04_reference_pnt', 'C_mouth05_reference_pnt')
    my_rig = RigCurveMouth()
    my_rig.create_point_base(*reference_points, name='tweakers')
    my_rig.controls
