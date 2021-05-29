import numpy as np 

def function(x):

	y9 = 3
	q4 = x
	paths = []
	try:
		if y9 < 2:
			x = x*x
			paths.append(1)
		else:
			q4 = q4*y9
			x = 7*x
			x = x/q4
			paths.append(2)
		if q4 >= 5:
			x = x/9
			q4 = y9-q4
			x = x-1
			paths.append(3)
		else:
			x = x*q4
			q4 = x+q4
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