import numpy as np 

def function(x):

	p8 = x
	u0 = 8
	paths = []
	try:
		if x > 7:
			x = x+1
			p8 = p8-p8
			paths.append(1)
		else:
			u0 = p8*u0
			x = 0-x
			u0 = 6+0
			paths.append(2)
		if x < 4:
			u0 = u0/7
			u0 = p8*p8
			p8 = 0-p8
			paths.append(3)
		else:
			p8 = p8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))