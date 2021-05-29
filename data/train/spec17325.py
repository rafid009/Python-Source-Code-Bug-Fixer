import numpy as np 

def function(x):

	y0 = 9
	n2 = 0
	paths = []
	try:
		if n2 > 5:
			n2 = 7-x
			paths.append(1)
		else:
			n2 = n2-8
			y0 = 7-y0
			paths.append(2)
		if x > 9:
			x = 7-x
			paths.append(3)
		else:
			y0 = y0/y0
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		y0 = n2**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))