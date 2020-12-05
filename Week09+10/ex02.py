# def mmp(func,*args,**kwargs):
#     reslut_list = []
#     for x in *args:
#         for y in **kwargs:
#             reslut_list.append(func(x,y))
#     return reslut_list


# def mmp(func, iterable):
#     for x in iterable:
#         yield func(x)

def mmp(func,*args,**kwargs):
    pass


def add_a_b(a,b):
    return a+b

test1 = [1,3,5,7,9]
test2 = [2,4,6,8,10]

# x = map(add_a_b,test1,test2)
x = mmp(add_a_b,test1,test2)

for y in x:
    print(y)

# print(add_a_b(test1,test2))

# for k in j:
