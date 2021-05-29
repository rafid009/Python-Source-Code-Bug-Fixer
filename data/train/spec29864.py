import numpy as np 

def function(x):

	d9 = 5
	x8 = 8
	paths = []
	try:
		if x >= 8:
			x8 = 9*4
			paths.append(1)
		else:
			x8 = x8+x
			paths.append(2)
		if d9 > 0:
			x8 = 4*x8
			paths.append(3)
		else:
			x = 4/d9
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))