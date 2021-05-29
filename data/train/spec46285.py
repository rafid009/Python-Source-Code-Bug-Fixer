import numpy as np 

def function(x):

	x0 = x
	j1 = x
	paths = []
	try:
		if x <= 8:
			j1 = j1-j1
			x0 = 4+x0
			paths.append(1)
		else:
			j1 = j1/j1
			paths.append(2)
		if x <= 3:
			x = 8*5
			paths.append(3)
		else:
			j1 = 5-j1
			x0 = x0*8
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))