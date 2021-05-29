import numpy as np 

def function(x):

	y7 = x
	s5 = x
	x = 7
	paths = []
	try:
		if y7 > 5:
			x = x-7
			s5 = 5/s5
			s5 = 3/s5
			paths.append(1)
		else:
			y7 = 0+7
			x = x-9
			y7 = 6/y7
			paths.append(2)
		if x > 0:
			y7 = 7-y7
			y7 = 4*x
			paths.append(3)
		else:
			y7 = y7*y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))