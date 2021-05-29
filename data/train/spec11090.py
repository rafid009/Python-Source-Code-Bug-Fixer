import numpy as np 

def function(x):

	u7 = 1
	x3 = 1
	paths = []
	try:
		if x > 4:
			x = x/u7
			u7 = 1/u7
			x3 = 8-x3
			paths.append(1)
		else:
			u7 = x*u7
			x3 = x3+x3
			paths.append(2)
		if u7 <= 2:
			u7 = 4/u7
			x3 = 8-6
			paths.append(3)
		else:
			x = x/x3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))