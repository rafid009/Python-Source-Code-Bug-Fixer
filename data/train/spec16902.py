import numpy as np 

def function(x):

	o4 = x
	u0 = x
	paths = []
	try:
		if u0 > 6:
			u0 = 1+9
			x = o4/x
			u0 = 0-u0
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if x <= 0:
			x = 1-7
			u0 = o4/x
			x = 6-x
			paths.append(3)
		else:
			u0 = u0/u0
			x = x*7
			u0 = 3-9
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