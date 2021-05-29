import numpy as np 

def function(x):

	u6 = 2
	y2 = x
	paths = []
	try:
		if y2 >= 5:
			x = y2*9
			y2 = y2-8
			paths.append(1)
		else:
			u6 = x/u6
			x = x*7
			paths.append(2)
		if u6 > 5:
			y2 = x/x
			paths.append(3)
		else:
			u6 = u6/x
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