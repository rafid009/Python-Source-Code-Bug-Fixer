import numpy as np 

def function(x):

	g8 = 2
	f2 = x
	paths = []
	try:
		if f2 >= 8:
			f2 = f2*g8
			x = g8+0
			paths.append(1)
		else:
			g8 = 8*g8
			g8 = 3+g8
			paths.append(2)
		if g8 <= 3:
			f2 = f2/9
			g8 = 8/g8
			x = g8/5
			paths.append(3)
		else:
			x = x+f2
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