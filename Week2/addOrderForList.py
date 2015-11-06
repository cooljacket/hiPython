# -*-codeing:utf8-*-
# 本次练习是读写文件，给一个列表加1,2,3,...这样的序号
# 默认打开文件使用缓存
# 但是对于大文件，一次性读取所有的行，有点不科学，后面学到with或生成器时会修正这个例子

fp = open(r'files/HelloList.txt', 'r')
lines = fp.readlines()
fp.close()

fp = open('files/HelloOrderList.txt', 'w')
i = 1
for line in lines:
    fp.write(str(i)+'. '+line)
    i = i + 1

fp.close()