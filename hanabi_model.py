import random

def CreateHanabiModel(x,y):
    # 花火の射出位置を設定
    firework_pos = (x, y, 0)


    # 70%で通常の球
    if random.randint(0, 100) < 70:
        bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=firework_pos, scale=(.5, .5, .5))
    
    # 30%でモンキーの球
    else:
        bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=firework_pos, scale=(.5, .5, .5))


if __name__ == '__main__':
    try:
        pos_X = p_x
        pos_Y = p_y
    except:
        pos_X = random.randint(-10, 10)
        pos_Y = random.randint(-10, 10)

    CreateHanabiModel(pos_X, pos_Y)