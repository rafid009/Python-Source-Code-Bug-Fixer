import numpy as np 

def function(x):

	y0 = x
	n6 = x
	paths = []
	try:
		if x > 9:
			n6 = y0+x
			paths.append(1)
		else:
			n6 = 2-n6
			x = x*y0
			paths.append(2)
		if n6 <= 5:
			y0 = n6-y0
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))