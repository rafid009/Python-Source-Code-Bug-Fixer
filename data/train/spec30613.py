import numpy as np 

def function(x):

	e0 = 6
	r2 = x
	paths = []
	try:
		if x >= 3:
			x = 1+9
			r2 = 5*r2
			paths.append(1)
		else:
			x = r2+1
			x = x+4
			paths.append(2)
		if x > 4:
			r2 = r2*x
			r2 = r2+6
			r2 = r2-3
			paths.append(3)
		else:
			e0 = e0-2
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