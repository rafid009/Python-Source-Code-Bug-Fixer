import numpy as np 

def function(x):

	y5 = 5
	i4 = x
	paths = []
	try:
		if x > 4:
			y5 = y5-y5
			paths.append(1)
		else:
			y5 = 2+y5
			x = 2*x
			y5 = 8/y5
			paths.append(2)
		if i4 < 8:
			y5 = y5-x
			paths.append(3)
		else:
			y5 = 5*y5
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		y5 = i4**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))