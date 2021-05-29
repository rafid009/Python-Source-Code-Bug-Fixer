import numpy as np 

def function(x):

	u4 = x
	x1 = x
	paths = []
	try:
		if u4 < 1:
			x = x+u4
			x1 = 3*x
			u4 = u4+6
			paths.append(1)
		else:
			x = 6+x
			x1 = x*x
			x1 = 8+x1
			paths.append(2)
		if x > 2:
			u4 = u4+4
			x1 = 9*x1
			u4 = 3-x1
			paths.append(3)
		else:
			x = u4+x
			x = x1/x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x1 = u4**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))