import numpy as np 

def function(x):

	o9 = x
	g4 = 2
	paths = []
	try:
		if o9 < 5:
			o9 = o9+g4
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if x < 7:
			o9 = 8+o9
			g4 = x+7
			paths.append(3)
		else:
			o9 = o9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))