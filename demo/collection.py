# list
expList = ['a', 'b', 'd', 'c', 'b']
# print(expList)
# print(len(expList)) # 长度
# print(expList[0])# 元素位置
# print(expList[-1])
# expList.append('z')
# expList.insert(0, '1')
# expList.pop(0)
# print(rlist)


# tuple 一旦初始化就不能修改
expTuple = (1,2,6,3)
# print(expTuple)
# expTuple.append(0) 禁止


# dict / map 使用键-值（key-value）存储
# dict内部存放的顺序和key放入的顺序是没有关系的, dict的key必须是不可变对象。
# 特点：查找和插入的速度极快，不会随着key的增加而变慢；
#       需要占用大量的内存，内存浪费多。
expDict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(expDict['Michael'])
# expDict['Michael'] = 100
# print(expDict['Michael'])
# print('Thomas' in expDict)
# # get方法 如果key不存在，可以返回None，或者自己指定的value
# print(expDict.get('Thomas'))
# print(expDict.get('Thomas', -1))


# set
expSetOri = {1, 0, 3}
# print(expSetOri)
# expSet = {1, 1, 2, 2, 3, 3}
# print(expSet)
# # 添加元素
# expSet.add(5)
# print(expSet)
# # 移除元素
# expSet.remove(5)
# print(expSet)
# # 运算
# print(expSetOri & expSet)
# print(expSetOri | expSet)

# # 错误实例
# t = (1,[2,3])
# s2 = set(t)
# set和dict的key值是根据传入的不可变值（数值型，字符串，元组），会对传入的key值进行hash计算，
# 所以传入的为list可变值，会产生TypeError错误，原因是“list”类型无法进行hash计算。



