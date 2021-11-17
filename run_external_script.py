import bpy
import random
import math

## 固定値設定 #############################################################
# ファイルパス一覧
FILE_ROOT_PATH = 'D:/blender_firework_py/'
material_file_name = FILE_ROOT_PATH + "material_firework.py"
particle_file_name = FILE_ROOT_PATH + "particle_firework.py"
animatio_file_name = FILE_ROOT_PATH + "firework_animation.py"
woshader_file_name = FILE_ROOT_PATH + "world_shader.py"
cameanim_file_name = FILE_ROOT_PATH + "camera_animation.py"

# 生み出す花火の個数を設定
FIREWORKS_NUM = 50

# シーンのエンドフレーム
FRAME_END = 600
##########################################################################

# レンダリング設定
bpy.data.scenes["Scene"].render.filepath = FILE_ROOT_PATH
bpy.data.scenes["Scene"].render.image_settings.file_format = "AVI_JPEG"

#オブジェクト全選択
bpy.ops.object.select_all(action='SELECT') 
#オブジェクト全削除
bpy.ops.object.delete(True)

# 回転はラジアンに直す必要があるので、そのための定数を用意
ROTATE = 2*math.pi/360

# カメラ配置
bpy.ops.object.camera_add(location=(0,0,75), rotation=(70*ROTATE, 0, 0))
bpy.data.objects[0].name = "Camera"

# Worldのシェーダーで星空を生成
exec(compile(open(woshader_file_name).read(), woshader_file_name, 'exec'))
bpy.context.scene.frame_end = FRAME_END

# カメラアニメーションを作成
exec(compile(open(cameanim_file_name).read(), cameanim_file_name, 'exec'))

for i in range(FIREWORKS_NUM):
    # 花火の色をランダムに設定
    firework_color = (random.random(), random.random(), random.random(), 1)

    # パーティクルに使用するオブジェクトのマテリアル作成
    exec(compile(open(material_file_name).read().replace("ANIM_COLOR", str(firework_color)), material_file_name, 'exec'))

    # パーティクルオブジェクトの名前を保持
    firework_particle_object_name = bpy.context.active_object.name

    # 花火の射出位置をランダムに設定
    firework_pos = (random.randint(-10, 10), random.randint(-10, 10), 0)
    
    # 花火本体を生成
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=firework_pos, scale=(1, 1, 1))

    # 花火の発射フレームをランダムに設定
    firework_start_frame = random.randint(0, FRAME_END - 100)

    # 花火パーティクル作成
    exec(compile(open(particle_file_name).read().replace("OBJ_NAME", firework_particle_object_name)
                                                .replace("ST_FR", str(firework_start_frame)), particle_file_name, 'exec'))

    # 花火アニメーション作成
    exec(compile(open(animatio_file_name).read().replace("ST_FR", str(firework_start_frame)), animatio_file_name, 'exec'))