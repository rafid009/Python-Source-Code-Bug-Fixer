import numpy as np 

def function(x):

	n0 = 0
	u0 = 4
	paths = []
	try:
		if u0 >= 3:
			n0 = x+n0
			paths.append(1)
		else:
			n0 = n0+7
			paths.append(2)
		if x > 8:
			x = u0/x
			x = x+7
			paths.append(3)
		else:
			u0 = u0-6
			x = 0*8
			x = u0/9
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