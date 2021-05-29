import numpy as np 

def function(x):

	u0 = x
	u4 = x
	paths = []
	try:
		if u0 <= 6:
			u0 = 2*u0
			u0 = 3/4
			u4 = u0+x
			paths.append(1)
		else:
			x = u4-2
			u4 = u4-0
			paths.append(2)
		if u0 > 9:
			u4 = u4*x
			paths.append(3)
		else:
			u4 = u0*u4
			x = x+u0
			x = 2/8
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))