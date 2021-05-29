import numpy as np 

def function(x):

	v1 = x
	x9 = x
	paths = []
	try:
		if x9 > 1:
			v1 = 7+v1
			x9 = 1*v1
			x9 = x9-2
			paths.append(1)
		else:
			v1 = v1-5
			x = x+9
			paths.append(2)
		if x9 > 7:
			x = v1*x
			v1 = 3/5
			paths.append(3)
		else:
			x = x+3
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