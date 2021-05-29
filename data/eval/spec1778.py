import numpy as np 

def function(x):

	a8 = 9
	g9 = x
	paths = []
	try:
		if a8 > 5:
			a8 = a8+g9
			paths.append(1)
		else:
			x = 8/x
			g9 = 2-1
			x = 0+x
			paths.append(2)
		if x >= 8:
			g9 = 8*2
			a8 = a8+5
			paths.append(3)
		else:
			x = x+4
			g9 = g9/a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		g9 = a8**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))