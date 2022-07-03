# This file was created by Wonseok Ryu (git hub id: johninkorea)

# announcement
print("여러명의 더치 페이 계산을 도와줍니다.")
print('금액을 입력할때 수학 기호를 사용할 수 있습니다.')

#input
b=[]
c=[]
while True:
    b[0:]=map(str,input("각 구성원의 이름을 공백으로 구분하여 입력해 주세요.").split( ))
    c[0:]=map(str ,input("각 구성원이 사용한 금액을 위의 순서와 같이 입력해주세요.").split( ))
    if len(b)!=len(c):
        print("사용 내용과 인원의 수가 같아야 합니다.\n다시 입력해주세요.")
        pass
    else:
        print('계산 결과는 다음과 같습니다.')
        break

# claculation
a=len(b)
c =[float(eval(x)) for x in c]
x=0
d=[]

while x<a:
	d.append(c[x]/a)
	x+=1

# print result
y=0
print("*"*50)
print()
while y<a:
    print("{}는 모두에게 {}원을 받아야합니다.".format(b[y],str(d[y])))
    y+=1
print("*"*50)

z=0
while z<a:
    print()
    print("{}입장에서는 ".format(b[z]))
    e=d[z]
    f=b[z]
    del b[z]
    del d[z]
    v=0
    while v<a-1:
        j=e-d[v]
        k=float(j)
        if j>0:
            h='원을 받습니다'
        elif j==0:
            h='가만히'
        else:
            h='원을 줍니다'
        print("{}에게 {}{}".format(b[v],int(abs(round(j,0))),h))
        v+=1
    d.insert(z,e)
    b.insert(z,f)
    z+=1
    print("*"*50)
print()
print("위의 결과는 소수점 아래 첫번째 자리에서 반올림한 수치입니다.")
