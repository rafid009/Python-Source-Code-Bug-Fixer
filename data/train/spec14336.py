import numpy as np 

def function(x):

	x0 = 1
	u6 = x
	x = x
	paths = []
	try:
		if x < 7:
			x = x0*u6
			paths.append(1)
		else:
			u6 = 2/u6
			x0 = u6*8
			paths.append(2)
		if u6 >= 6:
			x = x/x0
			x0 = 7/x0
			paths.append(3)
		else:
			x0 = x0+u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))