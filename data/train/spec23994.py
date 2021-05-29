import numpy as np 

def function(x):

	x9 = x
	d7 = x
	x = x
	paths = []
	try:
		if x >= 3:
			x9 = x9*6
			d7 = d7+3
			paths.append(1)
		else:
			x = x*x
			d7 = 3-8
			paths.append(2)
		if x < 2:
			x9 = x9*x
			paths.append(3)
		else:
			x = x/x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		d7 = x9**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))