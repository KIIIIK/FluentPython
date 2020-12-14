#使用列表推导计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts

#使用生成器表达式计算笛卡尔积
for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)







