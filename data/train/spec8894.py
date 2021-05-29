import numpy as np 

def function(x):

	y6 = x
	f3 = 3
	paths = []
	try:
		if f3 >= 3:
			f3 = y6*f3
			y6 = y6/8
			y6 = y6+6
			paths.append(1)
		else:
			f3 = x+4
			x = f3/4
			paths.append(2)
		if y6 > 2:
			f3 = 0/3
			paths.append(3)
		else:
			f3 = y6-f3
			x = 3-x
			f3 = f3*5
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))