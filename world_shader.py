def WorldShader():
    D = bpy.data
    world_shader_tree = D.worlds["World"].node_tree

    # カラーランプを追加
    colorRampNode = world_shader_tree.nodes.new(type='ShaderNodeValToRGB')
    colorRampNode.color_ramp.elements[0].position = 0.7

    # ノイズテクスチャを追加
    noiseTextureNode = world_shader_tree.nodes.new(type='ShaderNodeTexNoise')
    noiseTextureNode.inputs[2].default_value = 550

    # ノイズテクスチャの「係数」をカラーランプの「係数」に接続
    world_shader_tree.links.new(noiseTextureNode.outputs[0], colorRampNode.inputs[0])

    # カラーランプの「カラー」を背景の「カラー」に接続
    world_shader_tree.links.new(colorRampNode.outputs[0], world_shader_tree.nodes[1].inputs[0])

if __name__ == '__main__':
    WorldShader()