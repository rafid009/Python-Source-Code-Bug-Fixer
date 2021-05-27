import numpy as np 

def function(x):

	o9 = x
	e0 = x
	paths = []
	try:
		if x > 0:
			x = x+4
			x = x+4
			e0 = 0/8
			paths.append(1)
		else:
			e0 = e0*e0
			paths.append(2)
		if x >= 1:
			e0 = o9+7
			paths.append(3)
		else:
			e0 = 2-9
			x = 3*o9
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		o9 = e0**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))