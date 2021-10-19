while True:
	try:
		a=int(input("Enter 1st Numerator \n"))
		b=int(input("Enter Denominator \n"))
		c=int(input("Enter Numerator \n"))
		d=int(input("Enter Denominator \n"))
		m=max(b,d)
		while True:
			if m%b==0 and m%d==0:
				break
			m=m+1
		print("L.C.M iS "+str(m))
		k=int(m/b)
		l=int(m/d)
		e=(f"{a*k}   {c*l}    {a*k+c*l}\n ___+___  = ____\n{b*k}  {d*l}      {b*k}")
		print(e)
		print("-----------------------------------------------")
		asig_1=(a*k+c*l)
		asig_2=(b*k)
		if asig_2>asig_1:
			mn=asig_1
		else:
			mn=asig_2
		for i in range(1,mn+1):
			if asig_1%i==0 and asig_2%i==0:
				hcf=i
		divid=int(asig_1/hcf)
		print(divid)
		print("__Is Your answer")
		divid_2=int(asig_2/hcf)
		print(divid_2)
		
	except:
		print("《Only Numbers are allowed》")