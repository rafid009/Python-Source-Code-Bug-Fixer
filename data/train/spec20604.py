import numpy as np 

def function(x):

	u2 = 9
	q8 = 8
	paths = []
	try:
		if q8 >= 3:
			x = x*u2
			u2 = q8+3
			paths.append(1)
		else:
			q8 = q8+q8
			x = 1+6
			x = 2/x
			paths.append(2)
		if x > 9:
			q8 = x/x
			q8 = q8/6
			q8 = 6-8
			paths.append(3)
		else:
			u2 = 4-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))