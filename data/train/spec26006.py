import numpy as np 

def function(x):

	a8 = x
	g4 = x
	paths = []
	try:
		if x <= 5:
			a8 = 9/x
			x = x-6
			x = x-8
			paths.append(1)
		else:
			x = 5*x
			x = 1/1
			paths.append(2)
		if g4 >= 5:
			a8 = 8+a8
			x = x-9
			g4 = g4/3
			paths.append(3)
		else:
			x = x+2
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