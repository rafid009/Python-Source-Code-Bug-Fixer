import numpy as np 

def function(x):

	r9 = 1
	y5 = x
	paths = []
	try:
		if x > 7:
			x = r9+y5
			r9 = 0+y5
			paths.append(1)
		else:
			y5 = y5-x
			y5 = y5-r9
			paths.append(2)
		if y5 < 2:
			x = 6-x
			x = x-x
			paths.append(3)
		else:
			r9 = r9*9
			y5 = 5*x
			y5 = x*y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		r9 = y5**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))