import numpy as np 

def function(x):

	g7 = 5
	v8 = x
	x = x
	paths = []
	try:
		if v8 <= 3:
			v8 = v8/2
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x <= 2:
			v8 = 3+0
			paths.append(3)
		else:
			v8 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))