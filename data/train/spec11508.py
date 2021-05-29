import numpy as np 

def function(x):

	d1 = x
	x7 = 8
	paths = []
	try:
		if d1 > 5:
			x = x-x7
			paths.append(1)
		else:
			d1 = d1+x
			x = d1*x
			paths.append(2)
		if x > 3:
			d1 = x7-2
			paths.append(3)
		else:
			d1 = 8/d1
			x7 = 6-x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))