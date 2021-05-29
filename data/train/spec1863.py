import numpy as np 

def function(x):

	y7 = 5
	q0 = x
	paths = []
	try:
		if x >= 5:
			y7 = 3/y7
			paths.append(1)
		else:
			x = 5+x
			q0 = q0-q0
			x = x+y7
			paths.append(2)
		if q0 <= 9:
			y7 = y7-y7
			x = x*7
			paths.append(3)
		else:
			x = 3+x
			y7 = 2+y7
			y7 = y7+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))