import numpy as np 

def function(x):

	d9 = x
	u5 = x
	x = x
	paths = []
	try:
		if u5 > 6:
			x = 2/x
			paths.append(1)
		else:
			u5 = 7+u5
			paths.append(2)
		if u5 > 8:
			x = 2/x
			d9 = x*d9
			d9 = 0/x
			paths.append(3)
		else:
			u5 = 1+u5
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