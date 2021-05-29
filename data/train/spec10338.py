import numpy as np 

def function(x):

	x7 = 2
	u5 = 6
	paths = []
	try:
		if x < 3:
			x7 = 5-x
			x7 = x7+x7
			x7 = x7+3
			paths.append(1)
		else:
			x = x/8
			x7 = 9+2
			x7 = 3*7
			paths.append(2)
		if x > 4:
			x7 = 2/x7
			u5 = 4-u5
			x = x/7
			paths.append(3)
		else:
			u5 = 5*u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))