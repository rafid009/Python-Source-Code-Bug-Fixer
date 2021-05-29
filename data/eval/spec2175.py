import numpy as np 

def function(x):

	u6 = x
	q8 = x
	paths = []
	try:
		if q8 >= 9:
			q8 = 7/8
			paths.append(1)
		else:
			u6 = 8-u6
			paths.append(2)
		if u6 <= 5:
			x = x-q8
			paths.append(3)
		else:
			u6 = 2*u6
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))