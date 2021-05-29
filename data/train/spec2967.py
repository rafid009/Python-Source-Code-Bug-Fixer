import numpy as np 

def function(x):

	g0 = 2
	f7 = x
	paths = []
	try:
		if x <= 6:
			g0 = g0/g0
			paths.append(1)
		else:
			g0 = 1-g0
			f7 = f7+5
			paths.append(2)
		if x >= 1:
			g0 = g0-3
			f7 = f7+f7
			paths.append(3)
		else:
			f7 = 9-f7
			f7 = f7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))