import numpy as np 

def function(x):

	y5 = 7
	u1 = x
	paths = []
	try:
		if x >= 2:
			x = 2*5
			paths.append(1)
		else:
			x = 3*x
			y5 = 2*x
			paths.append(2)
		if y5 <= 3:
			u1 = 6+6
			x = 6/x
			y5 = y5+y5
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))