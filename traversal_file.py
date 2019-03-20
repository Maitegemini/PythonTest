import os

'''
dirpath : 根路径 (字符串)
dirnames : 路径下的所有目录名 (列表)
filenames : 路径下的所有非目录文件名 (列表)
'''
m, n = 0, 0

path = input('请输入要遍历的文件夹的绝对路径:')

for dirpath, dirnames, filenames in os.walk(path):

    # 遍历所有文件
    for file in filenames:

        # 获取文件后缀名
        index = file.rfind('.')

        # 遍历所有.java文件
        if file[index:] == '.java':
            m += 1

        # 遍历所有.xml文件
        if file[index:] == '.xml':
            n += 1
print('--------------------------')
print('该文件夹下.java文件共有:%d个' % m)
print('--------------------------')
print('该文件夹下.xml 文件共有:%d个' % n)
