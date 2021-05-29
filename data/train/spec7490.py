import numpy as np 

def function(x):

	q4 = x
	x0 = x
	paths = []
	try:
		if q4 < 4:
			x = q4/7
			paths.append(1)
		else:
			q4 = 6/q4
			q4 = x*q4
			x0 = 2-6
			paths.append(2)
		if x > 3:
			q4 = q4/q4
			paths.append(3)
		else:
			x = x+x
			x0 = x0-x
			x = 0*3
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))