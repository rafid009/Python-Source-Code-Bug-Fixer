import numpy as np 

def function(x):

	v8 = x
	e8 = x
	paths = []
	try:
		if v8 >= 9:
			e8 = 7+7
			paths.append(1)
		else:
			x = x-e8
			paths.append(2)
		if x >= 6:
			v8 = 8+4
			e8 = 4-v8
			paths.append(3)
		else:
			x = x-v8
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