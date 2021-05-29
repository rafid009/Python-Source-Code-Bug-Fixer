import numpy as np 

def function(x):

	y6 = x
	d4 = x
	paths = []
	try:
		if y6 >= 6:
			x = y6*y6
			paths.append(1)
		else:
			x = x*4
			x = 3*y6
			paths.append(2)
		if y6 > 9:
			x = x+2
			y6 = 6+0
			d4 = 4/1
			paths.append(3)
		else:
			d4 = y6*4
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