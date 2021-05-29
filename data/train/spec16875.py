import numpy as np 

def function(x):

	u0 = 6
	d9 = x
	paths = []
	try:
		if d9 > 6:
			u0 = x+d9
			x = 7/x
			paths.append(1)
		else:
			d9 = d9/d9
			u0 = 9-u0
			paths.append(2)
		if d9 > 5:
			u0 = 0/3
			d9 = u0/x
			x = u0*x
			paths.append(3)
		else:
			d9 = d9+8
			d9 = d9+9
			u0 = 9+1
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