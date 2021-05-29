import numpy as np 

def function(x):

	q3 = x
	y4 = x
	paths = []
	try:
		if x > 9:
			x = x+x
			q3 = q3/y4
			x = x+y4
			paths.append(1)
		else:
			x = x+x
			y4 = y4/8
			paths.append(2)
		if q3 >= 3:
			q3 = q3*q3
			paths.append(3)
		else:
			y4 = y4*5
			y4 = x-8
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))