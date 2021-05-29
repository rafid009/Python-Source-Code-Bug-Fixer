import numpy as np 

def function(x):

	a1 = 9
	u2 = x
	paths = []
	try:
		if u2 >= 5:
			u2 = u2+u2
			paths.append(1)
		else:
			u2 = u2+x
			u2 = 9+u2
			paths.append(2)
		if a1 < 2:
			x = 5-x
			paths.append(3)
		else:
			u2 = 5+u2
			u2 = 0+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))