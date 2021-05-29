import numpy as np 

def function(x):

	u7 = x
	n0 = x
	paths = []
	try:
		if n0 <= 9:
			x = x*3
			u7 = n0/9
			paths.append(1)
		else:
			x = x-4
			u7 = x+6
			paths.append(2)
		if n0 >= 1:
			u7 = 0+6
			n0 = 1+3
			u7 = x*n0
			paths.append(3)
		else:
			n0 = 5-n0
			n0 = 7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))