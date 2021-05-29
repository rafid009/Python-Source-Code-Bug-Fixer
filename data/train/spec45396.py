import numpy as np 

def function(x):

	u5 = 2
	q3 = 9
	paths = []
	try:
		if q3 <= 8:
			q3 = q3-9
			x = 8/x
			paths.append(1)
		else:
			u5 = q3*u5
			x = x-7
			paths.append(2)
		if x > 3:
			q3 = q3+5
			q3 = x/8
			paths.append(3)
		else:
			q3 = u5-u5
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