import numpy as np 

def function(x):

	x4 = x
	j1 = x
	paths = []
	try:
		if x < 5:
			j1 = j1/7
			j1 = j1+6
			paths.append(1)
		else:
			x4 = 0-x4
			paths.append(2)
		if x > 2:
			j1 = 6/j1
			x = x+j1
			paths.append(3)
		else:
			j1 = j1/j1
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))