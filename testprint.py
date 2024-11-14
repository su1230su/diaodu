import pickle
# 读取pkl文件,rb是读取二进制文件，而r是读取文本文件
file = open('pr=01-1n=70-100pn=5-10ms=2-11u=1-3.pickle', 'rb')
info = pickle.load(file)
print(info)  # 打印输出读取的数据，默认是pandas的dataFrame格式
