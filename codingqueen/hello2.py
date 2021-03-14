# movie_rank = ["dactor strange","spiderman","lucky"]
# movie_rank= movie_rank[0:2]
# print(movie_rank)

# lang1=["C","C++","JAVA"]
# lang2=["Python","Go","C#"]
# a= lang1+ lang2
# print(a)

# num=[1,2,3,4,5,6,7]
# print(max(num))
# print(min(num))

# num=[1,2,3,4,5,6,]
# print(sum(num))

# cook=['김밥','김치찌개','곱창','케이크','아메리카노','김치','된장찌개','떡볶이','커피']
# print(len(cook))

# num=(1, 3, 5, 7, 9)
# average=sum(num)/len(num)
# print(average)

# num=[1,2,3,4,5,6,7,8,9,10,11,12]
# print(num[1::2])

# num=[1,2,3,4,5,6,7,8,9,10,11,12]
# print(num[::-1])

# interest=['samsung','lg','sk','mirae','naver']
# result = ' '.join(interest)
# print(result)

# interest=['samsung','lg','sk','mirae','naver']
# result= '/'.join(interest)
# print(result)

# interest=['samsung','lg','sk','mirae','naver']
# print('\n'.join(interest))

# string='samsung/lg/naver'
# result=string.split('/')
# print(result)

# deta=[2,3,4,56,8,9,5]
# # deta.sort()
# # print(deta)

# deta2= sorted(deta)
# print(deta2[::-1])

# my_variable=()
# print(type(my_variable))
# print(len(my_variable))

# movie_rank=('dactorstrang','spiderman','lucky')
# print(movie_rank)

# a=(1, )
# print(a,type(a))


# t= 1,2,3,4
# print(type(t))

# t=('a','b','c')
# t=('A','b','c')
# print(t)

# interest=['g','d','sk']
# print(tuple(interest))

# temp=('apple','banana','cake')
# a=temp[0]
# b=temp[1]
# c=temp[2]
# print(a,b,c)

(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)

# a,b,*c=(0,1,2,3,4,5)
# print(a)
# print(b)
# print(c)

# scores=[8.8,8.9,8.7,5.6,9.9,7.8,4.5]
# scores.sort()

# a, *score, b= scores
# print(score)
# print(sum(score)/len(score)) 


# scores=[8.8,8.9,8.7,5.6,9.9,7.8,4.5]
# _, _, *valid_score = scores
# print(valid_score)

# scores=[8.8,8.9,8.7,5.6,9.9,7.8,4.5]
# _,*valid_score,_=scores
# print(scores[1:6])

# temp={}
# print(temp,type(temp))

# ice={"melon":1000,
#      "pole":1200,
#      "bbang": 1800}
# print(ice)

# ice={"melon":1000,
#      "pole":1200,
#      "bbang": 1800}
# ice["josu"]=1500
# ice["world"]=1200

# ice["melon"]=1300
# print(ice)

# del ice["melon"]
# print(ice)

# inventory= {"메로나":[300],
#             "비비빅":[400],
#             "죠스바":[250]}

# print(inventory["메로나"][0])
# print(inventory["메로나"][1])

# inventory["월드콘"]=[500,7]
# print(inventory)

# print(list(inventory.keys()))

# print(list(inventory.values()))

# ice={"p":300, "m":200, "l":600}
# price= ice.values()
# print(sum(price))

# ice={"p":300, "m":200, "l":600}
# new={'o':2700}
# ice.update(new)
# print(ice)

# keys=('apple','pear','peach')
# vals = (300,200,500)
# print(list(zip(keys,vals)))

date=['09/05','09/06','09/07','09/08','09/09']
close_price =[10500,10300,10100,10800,11000]
print(dict(zip(date,close_price)))