import numpy as np 

def function(x):

	r4 = x
	y7 = x
	paths = []
	try:
		if r4 <= 0:
			r4 = 7*r4
			paths.append(1)
		else:
			y7 = y7+r4
			paths.append(2)
		if y7 < 2:
			r4 = y7+3
			r4 = r4*r4
			paths.append(3)
		else:
			x = 7-x
			x = 7-x
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