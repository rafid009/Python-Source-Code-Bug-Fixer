import numpy as np 

def function(x):

	g4 = 2
	j9 = 1
	paths = []
	try:
		if x <= 2:
			g4 = g4-0
			j9 = g4+j9
			j9 = j9-x
			paths.append(1)
		else:
			g4 = 7-j9
			paths.append(2)
		if j9 >= 2:
			g4 = g4-6
			x = x/g4
			paths.append(3)
		else:
			j9 = j9-3
			g4 = j9-g4
			x = 1*g4
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