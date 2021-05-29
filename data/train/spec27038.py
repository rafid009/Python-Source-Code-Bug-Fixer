import numpy as np 

def function(x):

	j7 = 1
	v9 = x
	paths = []
	try:
		if x >= 0:
			j7 = 2+x
			x = 0/x
			v9 = v9*6
			paths.append(1)
		else:
			v9 = v9*7
			v9 = v9+v9
			j7 = 0*x
			paths.append(2)
		if x < 1:
			x = 2*x
			v9 = 3/1
			paths.append(3)
		else:
			j7 = 6-j7
			v9 = v9-6
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