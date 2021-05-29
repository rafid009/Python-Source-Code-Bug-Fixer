import numpy as np 

def function(x):

	b7 = x
	g9 = 8
	paths = []
	try:
		if x < 6:
			x = 9/7
			b7 = b7+b7
			paths.append(1)
		else:
			g9 = 4/g9
			paths.append(2)
		if x >= 0:
			x = x*b7
			paths.append(3)
		else:
			x = 5/3
			x = x/b7
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