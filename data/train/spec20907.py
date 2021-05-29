import numpy as np 

def function(x):

	y6 = x
	u9 = 3
	paths = []
	try:
		if y6 <= 5:
			u9 = u9/4
			u9 = u9*y6
			x = 0+x
			paths.append(1)
		else:
			x = 2/x
			y6 = x+y6
			paths.append(2)
		if y6 < 6:
			u9 = u9*1
			x = 3*u9
			u9 = u9/y6
			paths.append(3)
		else:
			y6 = 6*y6
			u9 = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))