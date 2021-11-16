def CameraAnimtion():
    C = bpy.context
    D = bpy.data

    # カメラの動き（円周上を1周する）
    bpy.ops.curve.primitive_nurbs_circle_add(location=(3, 0, 0), rotation=((3.1415/2), 0, 0))
    C.object.data.path_duration = 72

    camera = bpy.data.objects['Camera']
    ncircle = bpy.data.objects['NurbsCircle']

    camera.select = True
    ncircle.select = True

    C.scene.objects.active = ncircle #parent
    bpy.ops.object.parent_set(type='FOLLOW') #follow path

    # キーフレーム設定
    camera.select = True
    ncircle.select = False
    # bpy.context.scene.frame_current = 0 # set frame to 0
    # camera.location = (3,0,1) # set the location
    # bpy.ops.anim.keyframe_insert_menu(type='Location')

if __name__ == '__main__':
    CameraAnimtion()