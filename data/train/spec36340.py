import numpy as np 

def function(x):

	r5 = 1
	u0 = 5
	paths = []
	try:
		if r5 > 7:
			u0 = 5/8
			r5 = x-r5
			paths.append(1)
		else:
			r5 = 5*r5
			u0 = 9*u0
			x = 3/x
			paths.append(2)
		if u0 <= 3:
			r5 = 5*x
			x = 2-2
			r5 = 5-u0
			paths.append(3)
		else:
			x = x+9
			x = 0-x
			u0 = 1/u0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))