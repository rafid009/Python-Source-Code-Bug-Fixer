import numpy as np 

def function(x):

	j1 = x
	a0 = 4
	paths = []
	try:
		if j1 > 9:
			j1 = 4+x
			x = 8/8
			paths.append(1)
		else:
			j1 = 8+5
			paths.append(2)
		if j1 >= 6:
			a0 = 2+8
			paths.append(3)
		else:
			a0 = a0-1
			a0 = a0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))