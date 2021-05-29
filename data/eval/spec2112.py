import numpy as np 

def function(x):

	y6 = x
	b0 = x
	paths = []
	try:
		if y6 > 0:
			x = y6+1
			paths.append(1)
		else:
			x = 5*4
			x = 9-y6
			paths.append(2)
		if y6 > 4:
			y6 = 6-y6
			b0 = b0+1
			paths.append(3)
		else:
			x = 1+3
			x = y6*3
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