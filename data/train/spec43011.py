import numpy as np 

def function(x):

	q3 = 4
	b6 = 1
	paths = []
	try:
		if x < 4:
			x = x+x
			x = q3/x
			paths.append(1)
		else:
			x = x-q3
			paths.append(2)
		if q3 < 8:
			q3 = 0/2
			q3 = q3-4
			paths.append(3)
		else:
			q3 = 9-8
			q3 = q3*q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))