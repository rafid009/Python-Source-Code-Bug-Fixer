import numpy as np 

def function(x):

	d5 = x
	y3 = 2
	paths = []
	try:
		if x > 6:
			d5 = d5-x
			y3 = y3*y3
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if d5 < 5:
			y3 = d5-y3
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))