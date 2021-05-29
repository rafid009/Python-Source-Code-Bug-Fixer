import numpy as np 

def function(x):

	y8 = 7
	n7 = 6
	paths = []
	try:
		if n7 <= 9:
			n7 = 0*n7
			paths.append(1)
		else:
			y8 = x+y8
			paths.append(2)
		if n7 > 0:
			n7 = n7-1
			y8 = 3/y8
			x = 8-x
			paths.append(3)
		else:
			y8 = y8/6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))