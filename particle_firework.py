def ParticleFirework(material_object_name):
    # Blenderコンソールで準備されている短絡文字と同等のものを用意しておく
    C = bpy.context
    D = bpy.data

    # 現在アクティブ状態のオブジェクトを取得
    sphere_obj = C.active_object

    # スケールを調節
    sphere_obj.scale = [.5,.5,.5]

    # パーティクルシステムを追加
    bpy.ops.object.particle_system_add()

    # パーティクル設定を取得
    p_s = sphere_obj.particle_systems[0].settings

    # 放射
    p_s.count = 1000 
    p_s.frame_start = 50
    p_s.frame_end = 52
    p_s.lifetime = 70
    p_s.lifetime_random = 0.5

    # 放射>ソース
    p_s.emit_from = 'VOLUME'
    p_s.distribution = 'RAND'
    p_s.use_even_distribution = True

    # 速度
    p_s.normal_factor = 4.0

    # レンダー
    p_s.render_type = 'OBJECT'
    p_s.instance_object = D.objects[material_object_name]

    # フィールドの重み
    p_s.effector_weights.gravity = 0.4

if __name__ == '__main__':
    material_object_name = "OBJ_NAME"
    ParticleFirework(material_object_name)