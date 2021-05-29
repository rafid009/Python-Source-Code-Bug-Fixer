import numpy as np 

def function(x):

	u4 = x
	j4 = 0
	paths = []
	try:
		if x >= 0:
			u4 = 6/x
			paths.append(1)
		else:
			x = x+u4
			x = 9-x
			x = x-j4
			paths.append(2)
		if x <= 8:
			j4 = x*7
			x = 3-5
			x = x-9
			paths.append(3)
		else:
			u4 = u4-6
			u4 = 5*4
			u4 = 1*j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))