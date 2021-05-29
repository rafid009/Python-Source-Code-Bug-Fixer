import numpy as np 

def function(x):

	g1 = x
	y2 = 6
	paths = []
	try:
		if y2 >= 2:
			g1 = 0/g1
			y2 = x*x
			paths.append(1)
		else:
			y2 = 6*x
			paths.append(2)
		if g1 > 7:
			y2 = 8+y2
			y2 = y2-1
			paths.append(3)
		else:
			y2 = 5-y2
			x = x-1
			x = x*3
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		g1 = y2**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))