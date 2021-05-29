import numpy as np 

def function(x):

	b4 = x
	g9 = 9
	paths = []
	try:
		if g9 <= 2:
			g9 = 2*g9
			g9 = g9+3
			paths.append(1)
		else:
			g9 = g9*b4
			paths.append(2)
		if b4 >= 8:
			b4 = 6-5
			b4 = 3/b4
			x = b4-b4
			paths.append(3)
		else:
			g9 = 2-7
			b4 = b4*x
			x = x+1
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