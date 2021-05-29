import numpy as np 

def function(x):

	d4 = x
	a8 = 9
	paths = []
	try:
		if a8 >= 1:
			x = 5-x
			paths.append(1)
		else:
			x = 6*0
			paths.append(2)
		if x >= 1:
			x = a8+3
			paths.append(3)
		else:
			a8 = a8-8
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))