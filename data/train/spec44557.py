import numpy as np 

def function(x):

	g9 = 1
	v4 = x
	paths = []
	try:
		if g9 >= 6:
			x = x*x
			v4 = x+x
			paths.append(1)
		else:
			g9 = 4*v4
			paths.append(2)
		if g9 >= 5:
			x = 3*3
			paths.append(3)
		else:
			v4 = v4/g9
			v4 = v4*g9
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