import numpy as np 

def function(x):

	f7 = 6
	g8 = x
	paths = []
	try:
		if x <= 4:
			g8 = 8-f7
			g8 = 3/2
			f7 = x*x
			paths.append(1)
		else:
			f7 = 7+f7
			f7 = f7/2
			x = x*9
			paths.append(2)
		if g8 <= 9:
			f7 = x*7
			paths.append(3)
		else:
			f7 = 1*f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))