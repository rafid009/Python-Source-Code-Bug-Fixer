import numpy as np 

def function(x):

	e5 = x
	g9 = x
	x = x
	paths = []
	try:
		if e5 > 9:
			g9 = g9/g9
			x = 7*x
			paths.append(1)
		else:
			x = g9/x
			paths.append(2)
		if x > 9:
			g9 = 1+g9
			paths.append(3)
		else:
			g9 = 7-g9
			g9 = 1/x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))