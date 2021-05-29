import numpy as np 

def function(x):

	y5 = 4
	a5 = 6
	paths = []
	try:
		if a5 >= 3:
			a5 = a5-5
			a5 = x+8
			paths.append(1)
		else:
			y5 = 7/x
			y5 = x*y5
			y5 = y5-6
			paths.append(2)
		if y5 >= 8:
			x = x*6
			x = y5+x
			paths.append(3)
		else:
			y5 = 8/5
			a5 = y5/a5
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