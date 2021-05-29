import numpy as np 

def function(x):

	r8 = 3
	y5 = 7
	paths = []
	try:
		if r8 > 2:
			r8 = r8-x
			paths.append(1)
		else:
			r8 = x-6
			r8 = 5-8
			paths.append(2)
		if r8 < 8:
			x = y5*x
			y5 = x-6
			y5 = 5*9
			paths.append(3)
		else:
			y5 = 2-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))