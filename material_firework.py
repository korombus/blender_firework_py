def MaterialFirework(color):
    C = bpy.context
    D = bpy.data

    # オブジェクトを追加する
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, enter_editmode=False, align='WORLD', location=(0, 0, -10), scale=(1, 1, 1))
    
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
    emission.inputs[0].default_value = color

    # ノードを接続
    material_tree.links.new(emission.outputs[0], output.inputs[0])

    # マテリアルを追加
    C.object.data.materials.append(material_glass)

if __name__ == '__main__':
    color = ANIM_COLOR
    MaterialFirework(color)
