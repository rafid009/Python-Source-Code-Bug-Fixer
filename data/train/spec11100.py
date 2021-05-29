import numpy as np 

def function(x):

	e3 = x
	u7 = 2
	paths = []
	try:
		if u7 >= 3:
			e3 = 2/u7
			u7 = 9+u7
			paths.append(1)
		else:
			x = 3/x
			x = 0-e3
			paths.append(2)
		if e3 <= 6:
			e3 = e3+u7
			e3 = u7-e3
			u7 = 2*u7
			paths.append(3)
		else:
			x = 9*u7
			u7 = u7-3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))