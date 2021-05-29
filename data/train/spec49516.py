import numpy as np 

def function(x):

	x3 = x
	g9 = 7
	paths = []
	try:
		if x <= 0:
			x3 = x-3
			x = x*x3
			paths.append(1)
		else:
			g9 = x3*g9
			paths.append(2)
		if g9 <= 3:
			x = g9*x
			x3 = 0/x3
			paths.append(3)
		else:
			x = x-6
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))