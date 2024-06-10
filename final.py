def F2C(f):
    c=5*(f-32)/9
    return c
print("輸入格式(int,int) :")
left,right=map(int,input().split (','))
print("-----------------------------")
if left>right:
    print('error')
else:
    for f in range(left,right+1,2):
        print("{}:{:.2f}".format(f,F2C(f)))