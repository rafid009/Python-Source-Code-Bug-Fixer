import numpy as np 

def function(x):

	r1 = x
	y4 = x
	paths = []
	try:
		if r1 <= 2:
			x = x*8
			paths.append(1)
		else:
			y4 = 6/y4
			y4 = y4*7
			y4 = y4*y4
			paths.append(2)
		if x <= 9:
			x = 5/x
			paths.append(3)
		else:
			x = y4-5
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))