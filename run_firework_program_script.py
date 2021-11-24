import bpy
import random
import math
import json

## 固定値設定 #############################################################
# 実行ファイルパス一覧
FILE_ROOT_PATH = 'D:/blender_firework_py/'
setrendr_file_name = FILE_ROOT_PATH + "setting_render.py"
material_file_name = FILE_ROOT_PATH + "material_firework.py"
particle_file_name = FILE_ROOT_PATH + "particle_firework.py"
animatio_file_name = FILE_ROOT_PATH + "firework_animation.py"
woshader_file_name = FILE_ROOT_PATH + "world_shader.py"
hanamodl_file_name = FILE_ROOT_PATH + "hanabi_model.py"

# 再生用ファイル
firework_program_file_name = FILE_ROOT_PATH + "firework_program.py"

# SEファイルパス一覧
SE_ROOT_PATH = FILE_ROOT_PATH + 'se/'
sound_begin = (SE_ROOT_PATH + "花火・一発_begin.wav", SE_ROOT_PATH + "花火・一発_begin.wav")
sound_bomb = (SE_ROOT_PATH + "花火・一発_bomb.wav", SE_ROOT_PATH + "nc178345_bomb.wav")

# シーンのエンドフレーム
FRAME_END = 3600
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
bpy.ops.object.camera_add(location=(-80,0,0), rotation=(-70*ROTATE, 180*ROTATE, 90*ROTATE))
bpy.data.objects[0].name = "Camera"

# Worldのシェーダーで星空を生成
exec(compile(open(woshader_file_name).read(), woshader_file_name, 'exec'))
bpy.context.scene.frame_end = FRAME_END

# 再生用のファイルを読み込んで、アニメーションに反映
firework_program = {}
exec(compile(open(firework_program_file_name).read(), firework_program_file_name, 'exec'))

# フレームごとにkeyデータを読み出し
for frame_key in firework_program.keys():
    # key毎のデータを設定
    for program_data in firework_program[frame_key]:
        # 花火の色をランダムに設定
        firework_color = (random.random(), random.random(), random.random(), 1)
        # パーティクルに使用するオブジェクトのマテリアル作成
        exec(compile(open(material_file_name).read().replace("ANIM_COLOR", str(firework_color)), material_file_name, 'exec'))
        # パーティクルオブジェクトの名前を保持
        firework_particle_object_name = bpy.context.active_object.name
        
        # 花火本体を生成
        exec(compile(open(hanamodl_file_name).read().replace('p_x', str(program_data["x"]))
                                                    .replace('p_y', str(program_data["y"])), hanamodl_file_name, 'exec'))
        # 花火の発射フレームを設定
        firework_start_frame = frame_key
        # 花火パーティクル作成
        exec(compile(open(particle_file_name).read().replace("OBJ_NAME", firework_particle_object_name)
                                                    .replace("ST_FR", str(firework_start_frame)), particle_file_name, 'exec'))
        # 花火アニメーション作成
        exec(compile(open(animatio_file_name).read().replace("ST_FR", str(firework_start_frame))
                                                    .replace("SE_BG", str(sound_begin))
                                                    .replace("SE_BO", str(sound_bomb)), animatio_file_name, 'exec'))