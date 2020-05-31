"""from numpy import *
data = array([[1,2,3],[2,3,4]])
print(data)
size=data.shape
print(size)
random_nums=random.randint(low=0,high=10,size=(5,6))
print(random_nums)
col_vec=random_nums[:,(2,3,4)]
print(col_vec)
for i in range(0,col_vec.shape[0]):
    sum1=sum(col_vec[i])
    mean1=sum1/3"""
positive=30
negative=0
pos=(positive/(positive+negative))*2.5
neg=(negative/(positive+negative))*2.5
stars=pos+(2.5-neg)
print(stars)


