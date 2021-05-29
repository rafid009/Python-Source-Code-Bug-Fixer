import numpy as np 

def function(x):

	u0 = x
	y4 = 0
	paths = []
	try:
		if x < 1:
			u0 = u0+u0
			paths.append(1)
		else:
			y4 = 3-y4
			y4 = 5*1
			paths.append(2)
		if x < 4:
			x = 9/u0
			y4 = 0/7
			x = 8/x
			paths.append(3)
		else:
			y4 = x/y4
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		y4 = u0**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))