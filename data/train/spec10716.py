import numpy as np 

def function(x):

	y5 = x
	r1 = 9
	paths = []
	try:
		if r1 >= 0:
			r1 = 4*3
			r1 = x-6
			paths.append(1)
		else:
			y5 = 5*y5
			paths.append(2)
		if x >= 8:
			y5 = y5*7
			y5 = y5+y5
			paths.append(3)
		else:
			x = r1-x
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