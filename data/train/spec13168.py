import numpy as np 

def function(x):

	r2 = 4
	u6 = x
	paths = []
	try:
		if x < 7:
			u6 = u6*7
			paths.append(1)
		else:
			x = x*1
			r2 = r2/r2
			paths.append(2)
		if x < 3:
			x = r2-u6
			paths.append(3)
		else:
			r2 = x/r2
			u6 = 9-u6
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