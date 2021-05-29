import numpy as np 

def function(x):

	i7 = 0
	g6 = 2
	paths = []
	try:
		if i7 <= 4:
			g6 = g6+8
			i7 = 9*i7
			i7 = x/5
			paths.append(1)
		else:
			x = 6+9
			i7 = i7+i7
			paths.append(2)
		if x <= 4:
			x = x/1
			paths.append(3)
		else:
			g6 = 7/8
			i7 = i7/1
			g6 = 0-2
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