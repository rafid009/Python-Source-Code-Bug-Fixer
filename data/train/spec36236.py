import numpy as np 

def function(x):

	u5 = 6
	x0 = x
	paths = []
	try:
		if u5 <= 1:
			x = x*1
			paths.append(1)
		else:
			u5 = 1/u5
			paths.append(2)
		if u5 < 4:
			u5 = x-7
			x0 = x0*6
			x0 = x0-4
			paths.append(3)
		else:
			x = 9*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))