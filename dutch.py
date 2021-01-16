# This file was created by Wonseok Ryu (git hub id: johninkorea)

# announcement
print("여러명의 더치 페이 계산을 도와줍니다.")
print('금액을 입력할때 수학 기호를 포함하여도 계산해 드립니다')



#input
b=[]
c=[]
while True:
    b[0:]=map(str,input("각 인원의 이름을 공백을 활용하여 입력해주세요.").split( ))
    c[0:]=map(str ,input("각 인원이 사용한 금액을 순서대로 입력해주세요.").split( ))

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
