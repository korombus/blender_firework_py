import bpy
import random
import math

## 固定値設定 #############################################################
# 実行ファイルパス一覧
FILE_ROOT_PATH = 'D:/blender_firework_py/'
setrendr_file_name = FILE_ROOT_PATH + "setting_render.py"
material_file_name = FILE_ROOT_PATH + "material_firework.py"
particle_file_name = FILE_ROOT_PATH + "particle_firework.py"
animatio_file_name = FILE_ROOT_PATH + "firework_animation.py"
woshader_file_name = FILE_ROOT_PATH + "world_shader.py"
cameanim_file_name = FILE_ROOT_PATH + "camera_animation.py"
hanamodl_file_name = FILE_ROOT_PATH + "hanabi_model.py"

# SEファイルパス一覧
SE_ROOT_PATH = FILE_ROOT_PATH + 'se/'
sound_begin = (SE_ROOT_PATH + "花火・一発_begin.wav", SE_ROOT_PATH + "花火・一発_begin.wav")
sound_bomb = (SE_ROOT_PATH + "花火・一発_bomb.wav", SE_ROOT_PATH + "nc178345_bomb.wav")


# 生み出す花火の個数を設定
FIREWORKS_NUM = 50

# シーンのエンドフレーム
FRAME_END = 600
##########################################################################

# レンダリング設定
exec(compile(open(setrendr_file_name).read().replace("FILE_ROOT_PATH", FILE_ROOT_PATH), setrendr_file_name, 'exec'))

#オブジェクト全選択
bpy.ops.object.select_all(action='SELECT') 
#オブジェクト全削除
bpy.ops.object.delete(True)

# シーケンスエディタを生成
if bpy.context.scene.sequence_editor:
    bpy.context.scene.sequence_editor_clear()
bpy.context.scene.sequence_editor_create()

# 回転はラジアンに直す必要があるので、そのための定数を用意
ROTATE = 2*math.pi/360

# カメラ配置
bpy.ops.object.camera_add(location=(0,-150,36), rotation=(90*ROTATE, 0, 0))
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
    
    # 花火本体を生成
    exec(compile(open(hanamodl_file_name).read(), hanamodl_file_name, 'exec'))

    # 花火の発射フレームをランダムに設定
    firework_start_frame = random.randint(0, FRAME_END - 100)

    # 花火パーティクル作成
    exec(compile(open(particle_file_name).read().replace("OBJ_NAME", firework_particle_object_name)
                                                .replace("ST_FR", str(firework_start_frame)), particle_file_name, 'exec'))

    # 花火アニメーション作成
    exec(compile(open(animatio_file_name).read().replace("ST_FR", str(firework_start_frame))
                                                .replace("SE_BG", str(sound_begin))
                                                .replace("SE_BO", str(sound_bomb)), animatio_file_name, 'exec'))