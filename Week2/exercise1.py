# -*-codeing:utf8-*-
# 文件操作的练习

fp = open('files\src.txt', 'r')
contents = fp.readlines()
fp.close()

fp = open('files\dest.txt', 'w')
for line in contents:
	if line.find('\n') == -1:
		line += '\n'
	fp.write(line)
fp.close()

fp = open('files\dest.txt', 'a+')
for line in contents:
	if line.find('\n') == -1:
		line += '\n'
	fp.write(line)
fp.close()

fp = open('files\dest.txt', 'r')
fp.seek(15, 0)
print('From head:', fp.readline())
fp.seek(15, 1)
print('From current:', fp.readline())
fp.seek(-1, 2)
print('From tail:', fp.readline())
fp.close()
