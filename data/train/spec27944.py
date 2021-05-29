import numpy as np 

def function(x):

	x4 = 4
	p8 = x
	paths = []
	try:
		if x4 > 6:
			p8 = 4+x4
			x4 = 5-4
			paths.append(1)
		else:
			x = 8-p8
			p8 = p8+8
			paths.append(2)
		if x4 >= 3:
			x = x4-x
			paths.append(3)
		else:
			x = 0-p8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))