import numpy as np 

def function(x):

	x8 = 1
	n5 = 0
	paths = []
	try:
		if n5 > 0:
			x = x-5
			n5 = n5*1
			n5 = x/x
			paths.append(1)
		else:
			x8 = 9-3
			x = 0+x
			x = 8-x
			paths.append(2)
		if x > 3:
			x = x/3
			paths.append(3)
		else:
			n5 = n5/8
			n5 = x8*n5
			n5 = 6-n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))