import numpy as np 

def function(x):

	e4 = 4
	u7 = x
	paths = []
	try:
		if x <= 0:
			x = u7/5
			paths.append(1)
		else:
			e4 = 3*e4
			x = x-1
			e4 = e4+x
			paths.append(2)
		if x >= 9:
			x = x-u7
			x = x*3
			paths.append(3)
		else:
			u7 = u7+e4
			e4 = e4*7
			e4 = 3/u7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		e4 = u7**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))