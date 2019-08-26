# 三角形の面積
def triangle(base, height) :
    area = base * height / 2
    return area
    
# 関数を試す
b = 15    # 底辺
h = 13    # 高さ
v = triangle(b, h)    # 三角形の面積を求める
print(f"底辺{b}、高さ{h}の三角形の面積は{v :.1f}です。")

