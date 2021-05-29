import numpy as np 

def function(x):

	y1 = 8
	u5 = 7
	paths = []
	try:
		if x <= 1:
			u5 = u5/5
			u5 = u5-6
			x = u5-u5
			paths.append(1)
		else:
			u5 = x+8
			x = x-5
			paths.append(2)
		if y1 <= 8:
			u5 = y1/u5
			paths.append(3)
		else:
			x = 0+3
			u5 = u5-u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))