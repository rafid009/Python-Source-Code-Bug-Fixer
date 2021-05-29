import numpy as np 

def function(x):

	x1 = 7
	j8 = 3
	paths = []
	try:
		if j8 <= 7:
			x = 0*3
			j8 = j8-x1
			x = 0+j8
			paths.append(1)
		else:
			j8 = j8/1
			x = 4/x
			paths.append(2)
		if x < 2:
			x1 = x1-x
			paths.append(3)
		else:
			x = 1*5
			x1 = x1*x
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