import numpy as np 

def function(x):

	j1 = x
	g3 = 4
	paths = []
	try:
		if x >= 5:
			x = 5+g3
			paths.append(1)
		else:
			j1 = x-j1
			paths.append(2)
		if x >= 4:
			j1 = g3+5
			paths.append(3)
		else:
			j1 = 0+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))