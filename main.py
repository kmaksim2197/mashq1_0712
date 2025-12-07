# 1
lst=[-3,5,0,-1,7,2,-6]
step1=list(map(lambda x: 0 if x<0 else x, lst))
step2=list(map(lambda x: x*2, step1))
res=step2
print(res)

# 2
words=["cat","apple","car","hi","banana","map","aaa"]
step1=list(filter(lambda w: len(w)>3, words))
step2=list(filter(lambda w: 'a' in w, step1))
res=step2
print(res)
