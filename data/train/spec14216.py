import numpy as np 

def function(x):

	a0 = x
	r2 = x
	paths = []
	try:
		if a0 < 4:
			r2 = r2*r2
			paths.append(1)
		else:
			x = 1*7
			a0 = a0/r2
			r2 = 6-r2
			paths.append(2)
		if r2 > 1:
			r2 = r2*x
			r2 = r2*1
			paths.append(3)
		else:
			x = 6+6
			r2 = a0*r2
			r2 = 7/r2
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