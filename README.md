# Environment
- Blender 2.9x

# Usage
## 共通
1. Blenderを起動
1. Scriptingタブにて「該当するPythonファイル(下記参照)」を開く
1. 記述されている"FILE_ROOT_PATH"を自身の環境に合わせて変更
1. 「スクリプト実行ボタン」を押下
1. Animationタブにて「3Dビュー」を「レンダー」に変更
1. 再生ボタンを押して、アニメーションを確認

## 乱数花火アニメーションを再生
- Scriptingタブにて「run_external_script.py」を開く
## 固定花火アニメーションを再生
- Scriptingタブにて「run_firework_program_script.py」を開く

### 固定花火アニメーションの作り方
firework_program.jsonを変更してください。<br />
```
"start_frame_num": [
    {"x": X0, "y": Y0}
    {"x": X1, "y": Y1}
]
```
e.g.
``` 
"100": [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10}
],
"150": [
    {"x": 10, "y": -10},
    {"x": -10, "y": 10}
]
```
注: 同一フレーム内の前後関係は保証されません。<br />

作成時のヒント
```
x軸は、画面平面上で「上下」
y軸は、画面平面上で「左右」

x: -10 ~ 100
y: x=-10の時[-20 ~ 20]
   x=100の時[-50 ~ 50]

x:-10, y:20 ~ x:100, y:50の場合
y = 0.273x + 22.727

x:-10, y:-20 ~ x:100, y:-50の場合
y = -0.273x - 22.727

x:-10, y:20 ~ x:100, y:-50の場合
y = -0.636x + 13.636

x:-10, y:-20 ~ x:100, y:50の場合
y = 0.636x - 13.636
```

# License
## SE
### 花火
[ニコニ・コモンズ nc178345](https://commons.nicovideo.jp/material/nc178345)

[On-Jin ～音人～ 花火・一発](https://on-jin.com/sound/listshow.php?pagename=kan&title=%E8%8A%B1%E7%81%AB%E3%83%BB%E4%B8%80%E7%99%BA&janl=%E7%92%B0%E5%A2%83%E7%B3%BB%E9%9F%B3&bunr=%E8%8A%B1%E7%81%AB&kate=%E8%A1%97%E4%B8%AD%E3%83%BB%E7%94%BA%E4%B8%AD)