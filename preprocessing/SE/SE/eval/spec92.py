import numpy as np 

def function(x):

	i7 = x
	g4 = 5
	paths = []
	try:
		if x < 2:
			g4 = x-g4
			paths.append(1)
		else:
			i7 = 3-x
			paths.append(2)
		if g4 <= 1:
			g4 = 1+6
			g4 = g4*8
			paths.append(3)
		else:
			i7 = 4*i7
			g4 = 7-g4
			i7 = g4*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))