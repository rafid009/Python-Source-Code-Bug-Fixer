import numpy as np 

def function(x):

	p0 = 0
	b5 = x
	x = x
	paths = []
	try:
		if b5 < 0:
			p0 = 3*p0
			x = 8/x
			paths.append(1)
		else:
			p0 = p0*b5
			p0 = p0*x
			paths.append(2)
		if x >= 6:
			p0 = p0/4
			paths.append(3)
		else:
			p0 = p0/b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))