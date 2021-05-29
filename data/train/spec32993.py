import numpy as np 

def function(x):

	x6 = x
	u5 = x
	paths = []
	try:
		if x6 >= 2:
			u5 = 2*3
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x6 >= 6:
			x = 5*x
			paths.append(3)
		else:
			x6 = 9*x6
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