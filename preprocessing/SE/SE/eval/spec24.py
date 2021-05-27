import numpy as np 

def function(x):

	y0 = 6
	n9 = x
	paths = []
	try:
		if x <= 0:
			x = 8+6
			paths.append(1)
		else:
			n9 = n9/9
			paths.append(2)
		if n9 >= 4:
			x = x/x
			paths.append(3)
		else:
			y0 = 2*y0
			y0 = x/2
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))