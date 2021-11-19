import random

def CreateHanabiModel():
    # 花火の射出位置をランダムに設定
    firework_pos = (random.randint(-10, 10), random.randint(-10, 10), 0)


    # 70%で通常の球
    if random.randint(0, 100) < 70:
        bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=firework_pos, scale=(1, 1, 1))
    
    # 30%でモンキーの球
    else:
        bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=firework_pos, scale=(1, 1, 1))


if __name__ == '__main__':
    CreateHanabiModel()