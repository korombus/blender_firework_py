def SetFireworkBallMaterial():
    C = bpy.context
    D = bpy.data

    # マテリアルを新たに設定
    material_glass = D.materials.new('Firework')
    # ノードを使えるようにする
    material_glass.use_nodes = True
    material_tree = material_glass.node_tree

    # ノードの全削除
    for n in material_tree.nodes:
        material_tree.nodes.remove(n)

    # 出力ノードの作成
    output = material_tree.nodes.new(type='ShaderNodeOutputMaterial')
    output.location = (300, 0)

    # 放射ノードの作成
    emission = material_tree.nodes.new(type='ShaderNodeEmission')
    emission.location = (0, 0)
    # 色は赤色に設定。
    emission.inputs[0].default_value = (1, 0, 0, 1)

    # ノードを接続
    material_tree.links.new(emission.outputs[0], output.inputs[0])
    # マテリアルを追加
    C.object.data.materials.append(material_glass)

def fireworkAnimationToRiseup(C, D, sphere_obj):
    pass

def FireworkAnimationToBarn(C, D, sphere_obj):
    # アニメーションの最終キーフレーム
    animation_end_frame = 40

    # 打ち上げ終了までのキーフレームを設定
    # 初期フレーム - 花火玉は見えるようにしておく。
    C.scene.frame_set(0)
    sphere_obj.location = (sphere_obj.location.x, sphere_obj.location.y, 0)
    sphere_obj.show_instancer_for_viewport = True
    sphere_obj.show_instancer_for_render = True
    sphere_obj.keyframe_insert(data_path="location", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_viewport", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_render", index=-1)

    # 中間フレーム - ここまで一気に花火を上昇させる
    C.scene.frame_set(20)
    sphere_obj.location = (sphere_obj.location.x, sphere_obj.location.y, 30)
    sphere_obj.keyframe_insert(data_path="location", index=-1)

    # 最終フレーム - 花火玉は見えないようにしておく
    C.scene.frame_set(animation_end_frame)
    sphere_obj.location = (sphere_obj.location.x, sphere_obj.location.y, 40)
    sphere_obj.show_instancer_for_viewport = False
    sphere_obj.show_instancer_for_render = False
    sphere_obj.keyframe_insert(data_path="location", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_viewport", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_render", index=-1)

if __name__ == '__main__':
    # 花火玉本体のマテリアルを設定
    SetFireworkBallMaterial()

    C = bpy.context
    D = bpy.data

    # 現在アクティブ状態のオブジェクトを取得
    sphere_obj = C.active_object

    # 花火上昇時のアニメーションを作成
    fireworkAnimationToRiseup(C, D, sphere_obj)

    # 花火発破時のアニメーションを作成
    FireworkAnimationToBarn(C, D, sphere_obj)