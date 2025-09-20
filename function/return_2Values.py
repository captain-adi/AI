import math
def cal_areacur(r):
    area =  math.ceil(math.pi * (r ** 2))
    cir = math.ceil(2 * math.pi * r)
    return area,cir

a,c = cal_areacur(3)
print(f"area: {a} , cir   : {c}")