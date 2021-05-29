import numpy as np 

def function(x):

	y8 = x
	n3 = 1
	paths = []
	try:
		if n3 >= 9:
			y8 = x*3
			x = 8-x
			paths.append(1)
		else:
			y8 = 2*y8
			paths.append(2)
		if y8 > 6:
			x = n3/2
			x = x/7
			n3 = 7*n3
			paths.append(3)
		else:
			x = 7*x
			x = x/1
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