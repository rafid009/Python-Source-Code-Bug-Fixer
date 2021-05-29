import numpy as np 

def function(x):

	r2 = 9
	a4 = x
	x = 3
	paths = []
	try:
		if x <= 6:
			a4 = a4/4
			paths.append(1)
		else:
			r2 = r2/8
			paths.append(2)
		if a4 > 6:
			r2 = 6+r2
			x = x-0
			paths.append(3)
		else:
			r2 = r2+r2
			x = 5*a4
			a4 = 5*a4
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