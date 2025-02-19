import numpy as np 

def function(x):

	y4 = x
	n0 = x
	paths = []
	try:
		if y4 >= 7:
			y4 = 0-2
			y4 = y4+n0
			n0 = x+0
			paths.append(1)
		else:
			x = x/7
			x = x*x
			paths.append(2)
		if x < 6:
			n0 = y4-x
			n0 = n0/4
			paths.append(3)
		else:
			x = 9-x
			n0 = 1/1
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))