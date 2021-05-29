import numpy as np 

def function(x):

	g9 = 0
	t1 = 0
	paths = []
	try:
		if x < 2:
			x = x*2
			paths.append(1)
		else:
			g9 = 7-x
			paths.append(2)
		if t1 >= 8:
			x = x*6
			t1 = x/9
			g9 = g9+5
			paths.append(3)
		else:
			g9 = g9-g9
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