import numpy as np 

def function(x):

	c3 = x
	x8 = x
	paths = []
	try:
		if x < 2:
			x = 3*x
			paths.append(1)
		else:
			x = c3/1
			paths.append(2)
		if x < 7:
			x = x8/c3
			x = 2+x
			x = 6*x
			paths.append(3)
		else:
			x = x+1
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))