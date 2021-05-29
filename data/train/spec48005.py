import numpy as np 

def function(x):

	n3 = x
	u5 = 8
	paths = []
	try:
		if n3 < 8:
			x = 9+n3
			paths.append(1)
		else:
			u5 = 9*u5
			u5 = u5/9
			paths.append(2)
		if x <= 0:
			u5 = u5*6
			paths.append(3)
		else:
			x = 1+x
			n3 = 3/7
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