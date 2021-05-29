import numpy as np 

def function(x):

	r9 = x
	p0 = x
	paths = []
	try:
		if r9 <= 2:
			r9 = p0/8
			p0 = 1+p0
			paths.append(1)
		else:
			x = x*x
			x = 4/x
			paths.append(2)
		if x > 9:
			p0 = r9*p0
			p0 = r9/7
			p0 = p0*p0
			paths.append(3)
		else:
			r9 = x-8
			r9 = r9+r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))