import numpy as np 

def function(x):

	u0 = x
	v3 = x
	paths = []
	try:
		if u0 > 5:
			u0 = x*x
			paths.append(1)
		else:
			v3 = 6/v3
			x = x/x
			x = u0/u0
			paths.append(2)
		if v3 < 6:
			x = 1-6
			paths.append(3)
		else:
			v3 = x+3
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))