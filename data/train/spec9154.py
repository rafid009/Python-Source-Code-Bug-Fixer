import numpy as np 

def function(x):

	v4 = 8
	x6 = x
	paths = []
	try:
		if v4 >= 4:
			x = x+v4
			paths.append(1)
		else:
			x6 = 8+x
			paths.append(2)
		if x6 >= 1:
			x6 = 3/8
			v4 = 8/v4
			x = x-7
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))