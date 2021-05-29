import numpy as np 

def function(x):

	v9 = x
	v8 = 7
	paths = []
	try:
		if v8 >= 6:
			v9 = 6/v9
			x = 7-x
			paths.append(1)
		else:
			x = x-x
			v8 = v9/2
			paths.append(2)
		if x >= 0:
			x = 3-v9
			v8 = v8/2
			v8 = 6*v8
			paths.append(3)
		else:
			v9 = v9*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))