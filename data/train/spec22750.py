import numpy as np 

def function(x):

	x2 = x
	u9 = x
	paths = []
	try:
		if x <= 9:
			x2 = 6*u9
			u9 = 7/u9
			x2 = x-x2
			paths.append(1)
		else:
			x2 = 1*8
			paths.append(2)
		if x2 <= 6:
			x2 = x2-0
			paths.append(3)
		else:
			x2 = 9/x2
			x2 = 2*x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		u9 = x2**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))