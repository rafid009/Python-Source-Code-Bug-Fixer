import numpy as np 

def function(x):

	c3 = x
	v9 = 0
	x = 2
	paths = []
	try:
		if x <= 1:
			x = 6-2
			paths.append(1)
		else:
			x = x*2
			x = x*c3
			paths.append(2)
		if c3 <= 1:
			v9 = v9*1
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))