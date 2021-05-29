import numpy as np 

def function(x):

	q8 = x
	b7 = 7
	paths = []
	try:
		if x < 8:
			q8 = q8-3
			paths.append(1)
		else:
			q8 = 7/q8
			paths.append(2)
		if x < 0:
			b7 = b7-6
			b7 = x*6
			x = 5*x
			paths.append(3)
		else:
			x = x*q8
			x = 7*6
			q8 = 9-q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))