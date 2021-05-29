import numpy as np 

def function(x):

	e9 = 0
	j1 = 7
	paths = []
	try:
		if x >= 1:
			x = 4-7
			paths.append(1)
		else:
			e9 = 0*7
			j1 = 3*j1
			paths.append(2)
		if e9 > 4:
			x = j1/5
			paths.append(3)
		else:
			j1 = 9-9
			x = x-3
			e9 = 0-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))