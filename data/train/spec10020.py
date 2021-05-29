import numpy as np 

def function(x):

	x5 = 1
	i6 = 1
	paths = []
	try:
		if x5 > 3:
			i6 = 9*3
			x5 = x5/i6
			paths.append(1)
		else:
			x = 2*x
			x = x+9
			paths.append(2)
		if i6 > 6:
			i6 = i6*5
			paths.append(3)
		else:
			x = x/6
			x = 5*x
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