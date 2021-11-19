def ParticleFireworkToRaiseup(sphere_obj, material_object_name, firework_start_frame):
    bpy.ops.object.particle_system_add()
    
    p_s = sphere_obj.particle_systems[0].settings

    p_s.count = 100
    p_s.frame_start = firework_start_frame + 1
    p_s.frame_end = firework_start_frame + 35
    p_s.lifetime = 5
    
    # レンダー
    p_s.render_type = 'LINE'
    p_s.render_type = 'OBJECT'
    p_s.instance_object = D.objects[material_object_name]

    # フィールドの重み
    p_s.effector_weights.all = 0

def ParticleFireworkToBarn(C, D, sphere_obj, material_object_name, firework_start_frame):
    # パーティクルシステムを追加
    bpy.ops.object.particle_system_add()

    # パーティクル設定を取得
    p_s = sphere_obj.particle_systems[1].settings

    # 放射
    p_s.count = 1000 
    p_s.frame_start = firework_start_frame + 50
    p_s.frame_end = firework_start_frame + 52
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
    p_s.particle_size = 0.2
    p_s.instance_object = D.objects[material_object_name]

    # フィールドの重み
    p_s.effector_weights.gravity = 0.4

if __name__ == '__main__':
    material_object_name = "OBJ_NAME"
    firework_start_frame = ST_FR

    # Blenderコンソールで準備されている短絡文字と同等のものを用意しておく
    C = bpy.context
    D = bpy.data

    # 現在アクティブ状態のオブジェクトを取得
    sphere_obj = C.active_object

    # スケールを調節
    sphere_obj.scale = [.5,.5,.5]

    ParticleFireworkToRaiseup(sphere_obj, material_object_name, firework_start_frame);
    ParticleFireworkToBarn(C, D, sphere_obj, material_object_name, firework_start_frame)