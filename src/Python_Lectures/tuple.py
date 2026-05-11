from loguru import *
# t=['tata','honda','toyota','suzuki','vw','skoda','tata','tata']

# t=([1],[3,4],[6,7,8],[1,2],[1])
# # required o/p = (1,3,4,6,7,8,1,2,1)
# test_list=[]
# for i in t:
#     print(i)
#     test_list=test_list+i

# print(test_list)
# new_tuple=tuple(test_list)
# print(new_tuple)



t=(1,3,4,6,7,8,1,2,1)
t1=()
for i in t:
    t1=t1+((i**i),)
print(t1)