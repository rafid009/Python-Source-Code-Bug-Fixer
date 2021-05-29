import numpy as np 

def function(x):

	p1 = 4
	u5 = x
	paths = []
	try:
		if x >= 5:
			u5 = 0/u5
			p1 = p1*9
			paths.append(1)
		else:
			x = p1*x
			u5 = 8*0
			x = 0*p1
			paths.append(2)
		if x <= 9:
			p1 = x/p1
			paths.append(3)
		else:
			x = x-p1
			p1 = p1+1
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))