import numpy as np 

def function(x):

	a6 = 1
	g9 = 0
	paths = []
	try:
		if x <= 6:
			g9 = 9/4
			paths.append(1)
		else:
			a6 = 1/7
			x = 4+a6
			paths.append(2)
		if a6 <= 3:
			g9 = 5*g9
			a6 = a6+g9
			x = 8/x
			paths.append(3)
		else:
			x = a6*6
			a6 = 9*a6
			a6 = 8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))