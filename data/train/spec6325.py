import numpy as np 

def function(x):

	u9 = 4
	r2 = x
	paths = []
	try:
		if x >= 0:
			r2 = 0-r2
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x <= 0:
			x = r2-x
			r2 = 7-8
			paths.append(3)
		else:
			x = x*6
			r2 = 2+6
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