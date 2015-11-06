# -*-codeing:utf8-*-
# list的操作
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# 下标
print(week[1], week[-2])
# 正向切片（注意不取最后一位）
print(week[1:4])
print(week[-7:-2])
# 默认从0开始，如果不给出的话
print(week[:6])
# 可以设置步长
print(week[0::2])
# 逆序排列，其实就是从开始到结束，然后步长为-1，即反过来了
print(week[::-1])


# 一些运算和常用函数
print('Monday' in week)
print('Monday' not in week)
print(week[:3] + week[3:])
print(week[0:1]*3)


# 序列类型转换工厂函数
# list(), str(), unicode(), basestring(), tuple()
# 序列类型的内建函数：
# enumerate(), len(), max(), min(), reversed(), sorted(), sum(), zip()
