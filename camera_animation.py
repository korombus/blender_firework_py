def CameraAnimtion():
    C = bpy.context
    D = bpy.data

    # カメラが動くベジェ円を生成
    bpy.ops.curve.primitive_bezier_circle_add(enter_editmode=False, align='WORLD', scale=(25, 25, 1))
    bezier_obj = C.active_object
    bezier_obj.scale = (25, 25, 1)
    bpy.data.curves[bezier_obj.name].path_duration = int(bpy.context.scene.frame_end / 2)

    # カメラのターゲットとなるオブジェクトを生成
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 33), scale=(1, 1, 1))
    square_obj = C.active_object
    # ターゲットオブジェクトは見えないようにしておく
    square_obj.hide_viewport = True
    square_obj.hide_render = True

    # カメラのConstraintsを設定
    camera = bpy.data.objects["Camera"]
    camera.constraints.new(type="FOLLOW_PATH")
    camera.constraints.active.target = bezier_obj

    # constraintの「FOLLOW_PATH」に存在しているパスアニメーションのボタンを押したいが
    # カメラオブジェクトをview_layerでactiveにした上で
    # bpy.ops.constraintをカメラに設定したconstraintでオーバーライドしてあげないとボタンと同等の機能を指定できない。
    # なので、bpy.ops.constraintの向き先を強制的にカメラのconstraintに切り替えた上でアニメーションを設定する
    bpy.context.view_layer.objects.active = camera
    override={'constraint': camera.constraints.active}
    bpy.ops.constraint.followpath_path_animate(override, constraint=camera.constraints.active.name)

    camera.constraints.new(type="TRACK_TO")
    camera.constraints.active.target = square_obj

if __name__ == '__main__':
    CameraAnimtion()