from RMPY.rig import rigUVPin
import pymel.core as pm

def follow_surface():
    new_uv_pin = rigUVPin.RigUVPin()
    new_uv_pin.create_point_base('locator1', geometry='pSphere1')
    pm.matchTransform('pCube1', new_uv_pin.tip )
    pm.parentConstraint('pCube1', new_uv_pin.tip)

    # new_uv_pin.clean_up()

if __name__ == '__main__':
    follow_surface()