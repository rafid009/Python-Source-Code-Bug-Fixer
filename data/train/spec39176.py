import numpy as np 

def function(x):

	y6 = 0
	u0 = 6
	paths = []
	try:
		if u0 < 9:
			y6 = y6*1
			u0 = 4*x
			y6 = y6+x
			paths.append(1)
		else:
			y6 = 3+y6
			paths.append(2)
		if x >= 8:
			x = u0/9
			paths.append(3)
		else:
			u0 = 8/3
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		u0 = y6**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))