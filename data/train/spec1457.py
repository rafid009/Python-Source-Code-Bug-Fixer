import numpy as np 

def function(x):

	x1 = x
	v8 = x
	paths = []
	try:
		if x1 > 2:
			v8 = v8/v8
			x1 = v8*x
			paths.append(1)
		else:
			x1 = 6-x1
			x1 = x1-1
			x1 = x1*0
			paths.append(2)
		if x1 > 3:
			x1 = x1*v8
			paths.append(3)
		else:
			x1 = x1-3
			x = x-7
			x = x/v8
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