import numpy as np 

def function(x):

	u2 = 1
	e3 = x
	paths = []
	try:
		if x >= 3:
			u2 = 2+2
			x = e3+x
			x = 9+x
			paths.append(1)
		else:
			x = e3-9
			u2 = 7-u2
			u2 = u2-7
			paths.append(2)
		if x < 5:
			u2 = 7+u2
			x = 6/x
			paths.append(3)
		else:
			u2 = u2/9
			x = u2/e3
			e3 = 7+u2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))