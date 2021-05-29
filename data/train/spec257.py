import numpy as np 

def function(x):

	u7 = x
	e7 = 0
	paths = []
	try:
		if u7 <= 7:
			x = 1/x
			paths.append(1)
		else:
			e7 = 7+u7
			paths.append(2)
		if e7 <= 4:
			e7 = e7/x
			u7 = 5+u7
			e7 = 0*e7
			paths.append(3)
		else:
			x = u7-6
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