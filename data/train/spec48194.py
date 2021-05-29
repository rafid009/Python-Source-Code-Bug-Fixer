import numpy as np 

def function(x):

	u0 = 4
	d1 = x
	paths = []
	try:
		if x <= 6:
			u0 = 7+u0
			x = 8/x
			paths.append(1)
		else:
			d1 = u0+d1
			paths.append(2)
		if d1 < 2:
			x = x+u0
			paths.append(3)
		else:
			d1 = d1+4
			d1 = d1/6
			u0 = u0-8
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