def cround(a,b,action):
	a1=str(float(a))
	b1=str(float(b))
	a1=a1.split(".")[1]
	b1=b1.split(".")[1]
	n=max(len(a1),len(b1))
	return round(eval(str(a)+action+str(b)),n)
