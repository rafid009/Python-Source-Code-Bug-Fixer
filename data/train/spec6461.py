import numpy as np 

def function(x):

	u0 = x
	d4 = x
	paths = []
	try:
		if u0 <= 2:
			x = x*u0
			paths.append(1)
		else:
			u0 = u0*5
			d4 = d4+7
			paths.append(2)
		if u0 >= 6:
			u0 = 1+6
			d4 = 0/d4
			paths.append(3)
		else:
			d4 = 0/d4
			x = x-8
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))