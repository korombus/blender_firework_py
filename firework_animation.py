import random

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
    # 放射の強さを設定。
    emission.inputs[1].default_value = 0.4

    # カラーランプの作成
    color_ramp = material_tree.nodes.new(type='ShaderNodeValToRGB')
    color_ramp.location = (-300, 0)
    # 色を設定。
    color_ramp.color_ramp.elements[0].color = (1, 0.45, 0, 1)

    # レイヤーウェイトを作成
    layer_weight = material_tree.nodes.new(type='ShaderNodeLayerWeight')
    layer_weight.location = (-600, 0)
    # ブレンドを設定。
    layer_weight.inputs[0].default_value = 0.6

    # ノードを接続
    # レイヤーウェイト -> カラーランプ
    material_tree.links.new(layer_weight.outputs[1], color_ramp.inputs[0])

    # カラーランプ -> 放射
    material_tree.links.new(color_ramp.outputs[0], emission.inputs[0])

    # 放射 -> 出力
    material_tree.links.new(emission.outputs[0], output.inputs[0])

    # マテリアルを追加
    C.object.data.materials.append(material_glass)

def FireworkAnimation(C, D, sphere_obj, firework_start_frame, firework_se_begin, firework_se_bomb):
    # アニメーションの最終キーフレーム
    animation_end_frame = firework_start_frame + 40

    # 打ち上げ終了までのキーフレームを設定
    # 初期フレーム - 花火玉は見えないようにしておく
    C.scene.frame_set(0)
    sphere_obj.location = (sphere_obj.location.x, sphere_obj.location.y, 0)
    sphere_obj.show_instancer_for_viewport = False
    sphere_obj.show_instancer_for_render = False
    sphere_obj.keyframe_insert(data_path="location", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_viewport", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_render", index=-1)

    # 打ち出し開始フレーム - 花火玉を出現させる
    C.scene.frame_set(firework_start_frame)
    sphere_obj.location = (sphere_obj.location.x, sphere_obj.location.y, 0)
    sphere_obj.show_instancer_for_viewport = True
    sphere_obj.show_instancer_for_render = True
    sphere_obj.keyframe_insert(data_path="location", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_viewport", index=-1)
    sphere_obj.keyframe_insert(data_path="show_instancer_for_render", index=-1)

    # 中間フレーム - ここまで一気に花火を上昇させる
    C.scene.frame_set(firework_start_frame + 20)
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

    # 花火のSEを付ける
    # 花火玉をアクティブにする
    C.view_layer.objects.active = sphere_obj

    # 花火玉の名前の番号でチャンネルを割り振るようにする
    sphere_channel = ((int(len(C.scene.sequence_editor.sequences) / 2)) % 32) + 1

    # 花火が開くのは、アニメーション最終フレームから10フレ後なので、合わせる
    particle_start_frame = animation_end_frame + 10
    
    # 打ち上げSE
    C.scene.sequence_editor.sequences.new_sound(name="Begin", filepath=firework_se_begin[random.randint(0, len(firework_se_begin) - 1)], channel=sphere_channel, frame_start=firework_start_frame)
    # 爆発SE
    C.scene.sequence_editor.sequences.new_sound(name="Bomb", filepath=firework_se_bomb[random.randint(0, len(firework_se_bomb) - 1)], channel=sphere_channel, frame_start=particle_start_frame)

if __name__ == '__main__':
    firework_start_frame = ST_FR
    firework_se_begin = SE_BG
    firework_se_bomb = SE_BO

    # 花火玉本体のマテリアルを設定
    SetFireworkBallMaterial()

    C = bpy.context
    D = bpy.data

    # 現在アクティブ状態のオブジェクトを取得
    sphere_obj = C.active_object

    # 花火のアニメーションを作成
    FireworkAnimation(C, D, sphere_obj, firework_start_frame, firework_se_begin, firework_se_bomb)