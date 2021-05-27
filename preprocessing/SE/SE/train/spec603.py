import numpy as np 

def function(x):

	g1 = x
	y4 = x
	paths = []
	try:
		if g1 > 8:
			x = x/5
			paths.append(1)
		else:
			y4 = 6*y4
			x = x*g1
			paths.append(2)
		if y4 >= 8:
			y4 = 5/4
			paths.append(3)
		else:
			y4 = x-8
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))