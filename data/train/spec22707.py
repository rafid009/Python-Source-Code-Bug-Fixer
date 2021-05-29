import numpy as np 

def function(x):

	a2 = 2
	g9 = 1
	paths = []
	try:
		if a2 <= 3:
			a2 = a2/9
			paths.append(1)
		else:
			g9 = 5-g9
			a2 = a2-a2
			paths.append(2)
		if a2 <= 5:
			g9 = a2/1
			g9 = g9/1
			paths.append(3)
		else:
			a2 = a2-3
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