import numpy as np 

def function(x):

	o2 = x
	g9 = 4
	paths = []
	try:
		if o2 > 6:
			g9 = g9/1
			g9 = g9-g9
			paths.append(1)
		else:
			g9 = g9/9
			g9 = o2+g9
			paths.append(2)
		if x > 2:
			g9 = 8+g9
			x = x+g9
			x = 9-9
			paths.append(3)
		else:
			x = 7*g9
			o2 = x-o2
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