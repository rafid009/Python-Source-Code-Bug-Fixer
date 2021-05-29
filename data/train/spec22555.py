import numpy as np 

def function(x):

	f7 = 6
	g9 = 2
	paths = []
	try:
		if f7 > 3:
			g9 = g9+4
			f7 = 2/f7
			x = 2/x
			paths.append(1)
		else:
			x = x-8
			f7 = f7*0
			paths.append(2)
		if f7 < 7:
			f7 = f7-g9
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))