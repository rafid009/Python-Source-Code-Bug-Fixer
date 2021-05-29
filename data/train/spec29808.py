import numpy as np 

def function(x):

	g6 = 9
	i2 = x
	paths = []
	try:
		if i2 > 1:
			i2 = g6+4
			paths.append(1)
		else:
			x = x-g6
			x = g6*x
			paths.append(2)
		if i2 >= 3:
			i2 = x+x
			g6 = 6+i2
			paths.append(3)
		else:
			g6 = 5-x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		g6 = i2**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))