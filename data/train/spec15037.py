import numpy as np 

def function(x):

	g1 = x
	i2 = x
	paths = []
	try:
		if g1 < 7:
			x = x-8
			paths.append(1)
		else:
			g1 = g1+2
			i2 = i2-g1
			paths.append(2)
		if i2 >= 9:
			x = x+g1
			paths.append(3)
		else:
			g1 = g1-6
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		g1 = i2**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))