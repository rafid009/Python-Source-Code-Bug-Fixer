import numpy as np 

def function(x):

	e9 = 0
	j1 = 5
	paths = []
	try:
		if e9 >= 7:
			e9 = 8+2
			j1 = 8/j1
			paths.append(1)
		else:
			e9 = x-7
			j1 = e9/j1
			e9 = x*3
			paths.append(2)
		if j1 <= 5:
			e9 = 7/x
			paths.append(3)
		else:
			x = 0-x
			x = 5-x
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