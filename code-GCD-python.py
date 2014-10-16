num1,num2=map(int,raw_input().split())

d,b=num1,num2

while d>0:

	r=b%d

	b=d

	d=r

print b
