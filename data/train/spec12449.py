import numpy as np 

def function(x):

	k4 = 4
	o6 = x
	x = x
	paths = []
	try:
		if x <= 6:
			x = 2*x
			paths.append(1)
		else:
			x = 1+x
			x = x+4
			paths.append(2)
		if o6 <= 1:
			o6 = o6-2
			k4 = 3+o6
			k4 = k4*5
			paths.append(3)
		else:
			x = x-5
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))