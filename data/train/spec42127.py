import numpy as np 

def function(x):

	r2 = x
	p0 = 4
	paths = []
	try:
		if p0 > 4:
			r2 = p0-0
			r2 = r2*7
			x = p0*0
			paths.append(1)
		else:
			p0 = 6/p0
			paths.append(2)
		if x >= 5:
			r2 = 4/r2
			paths.append(3)
		else:
			r2 = 5-r2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))