def cround(a,b,action):
	a1=str(a)
	a2=str(b)
	try:
		a1=a1.split(".")[1]
		a2=a2.split(".")[1]
		n=max(len(a1),len(a2))
	except:
		n=0
	return round(eval(str(a)+action+str(b)),n)