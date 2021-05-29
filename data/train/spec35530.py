import numpy as np 

def function(x):

	v1 = 5
	b3 = 9
	paths = []
	try:
		if x > 0:
			x = 0*b3
			x = 6/9
			v1 = 9/v1
			paths.append(1)
		else:
			b3 = b3-b3
			paths.append(2)
		if x < 7:
			b3 = 9-b3
			v1 = v1*9
			paths.append(3)
		else:
			b3 = 9/7
			x = 9+6
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