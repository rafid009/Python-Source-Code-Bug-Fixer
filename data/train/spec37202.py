import numpy as np 

def function(x):

	u1 = x
	p3 = x
	paths = []
	try:
		if x >= 4:
			p3 = 2/8
			paths.append(1)
		else:
			p3 = u1+5
			paths.append(2)
		if p3 <= 0:
			p3 = 5+p3
			p3 = p3+2
			u1 = x-0
			paths.append(3)
		else:
			p3 = p3*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))