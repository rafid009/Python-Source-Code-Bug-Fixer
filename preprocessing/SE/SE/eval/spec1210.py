import numpy as np 

def function(x):

	g6 = x
	i4 = 1
	paths = []
	try:
		if i4 > 2:
			g6 = 6-g6
			paths.append(1)
		else:
			g6 = i4+5
			g6 = 9*6
			paths.append(2)
		if g6 <= 4:
			g6 = 2+g6
			x = 6/x
			x = x+x
			paths.append(3)
		else:
			x = 1*x
			x = x-0
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))