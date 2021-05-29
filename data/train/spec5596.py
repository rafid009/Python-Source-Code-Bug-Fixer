import numpy as np 

def function(x):

	w9 = x
	u0 = x
	paths = []
	try:
		if x <= 8:
			u0 = w9*4
			paths.append(1)
		else:
			x = 5-x
			x = 4/u0
			paths.append(2)
		if x <= 7:
			u0 = u0+7
			paths.append(3)
		else:
			u0 = u0*9
			w9 = w9-7
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