import numpy as np 

def function(x):

	u2 = 4
	u5 = x
	paths = []
	try:
		if u5 > 1:
			u2 = u5-u2
			paths.append(1)
		else:
			u5 = u5+3
			paths.append(2)
		if u5 > 3:
			u5 = u5-9
			x = x-3
			u5 = 8+u5
			paths.append(3)
		else:
			u5 = u5+u2
			x = 9-u5
			u5 = u5*u5
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))