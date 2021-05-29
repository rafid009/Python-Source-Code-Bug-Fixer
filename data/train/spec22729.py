import numpy as np 

def function(x):

	q4 = x
	x3 = x
	paths = []
	try:
		if x3 < 6:
			q4 = q4*q4
			paths.append(1)
		else:
			q4 = 9*q4
			x = 5+x
			q4 = q4*8
			paths.append(2)
		if q4 >= 2:
			q4 = x+q4
			paths.append(3)
		else:
			x = 4+x
			x3 = x3/9
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