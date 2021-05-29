import numpy as np 

def function(x):

	x3 = 9
	i2 = x
	paths = []
	try:
		if x >= 2:
			x3 = 1*x3
			x = x+7
			paths.append(1)
		else:
			i2 = i2+7
			x = x/x3
			x = i2/x
			paths.append(2)
		if x < 3:
			i2 = 5*3
			i2 = i2*6
			x3 = 2-x3
			paths.append(3)
		else:
			i2 = 4*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))