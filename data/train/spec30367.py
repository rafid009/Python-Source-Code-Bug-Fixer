import numpy as np 

def function(x):

	g5 = 6
	l8 = x
	paths = []
	try:
		if g5 < 3:
			x = l8+x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if l8 <= 6:
			g5 = g5-8
			paths.append(3)
		else:
			g5 = 8-5
			g5 = x+5
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))