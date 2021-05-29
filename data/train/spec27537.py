import numpy as np 

def function(x):

	d1 = 3
	u5 = 9
	paths = []
	try:
		if x < 6:
			u5 = d1-6
			u5 = 7-d1
			x = x*6
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if x >= 2:
			x = x-6
			paths.append(3)
		else:
			d1 = d1+5
			x = 6-x
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