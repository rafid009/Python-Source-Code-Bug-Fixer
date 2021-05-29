import numpy as np 

def function(x):

	y6 = x
	j1 = 3
	paths = []
	try:
		if j1 < 4:
			x = x-2
			j1 = 7*j1
			y6 = x*y6
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if y6 < 7:
			x = 9+x
			x = 1*x
			paths.append(3)
		else:
			y6 = x*3
			x = 0+2
			y6 = y6/x
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