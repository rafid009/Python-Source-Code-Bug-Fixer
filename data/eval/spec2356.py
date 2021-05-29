import numpy as np 

def function(x):

	y3 = 1
	d7 = x
	paths = []
	try:
		if x < 4:
			y3 = y3+8
			paths.append(1)
		else:
			x = d7*x
			y3 = 1*y3
			paths.append(2)
		if d7 < 0:
			d7 = 3/d7
			d7 = 6/d7
			paths.append(3)
		else:
			d7 = 9/d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		y3 = d7**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))