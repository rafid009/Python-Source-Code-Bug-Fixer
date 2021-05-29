import numpy as np 

def function(x):

	y6 = x
	u6 = 4
	paths = []
	try:
		if x <= 0:
			y6 = u6*6
			y6 = y6/3
			u6 = 8-0
			paths.append(1)
		else:
			x = x/6
			y6 = u6/5
			x = 1/x
			paths.append(2)
		if y6 >= 9:
			x = x/4
			paths.append(3)
		else:
			y6 = u6+y6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))