import numpy as np 

def function(x):

	u5 = x
	n5 = x
	paths = []
	try:
		if x > 7:
			n5 = n5/n5
			x = 9-x
			n5 = n5-u5
			paths.append(1)
		else:
			n5 = n5-3
			n5 = 7-7
			u5 = n5-u5
			paths.append(2)
		if x <= 9:
			u5 = 0-u5
			u5 = 9*u5
			paths.append(3)
		else:
			u5 = 8+u5
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))