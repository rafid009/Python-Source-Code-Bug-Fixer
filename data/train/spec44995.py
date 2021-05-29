import numpy as np 

def function(x):

	x9 = 8
	y6 = x
	x = 2
	paths = []
	try:
		if x9 >= 4:
			x = x/9
			y6 = x9+4
			x = x9*x
			paths.append(1)
		else:
			x = x*6
			x9 = 9+x9
			paths.append(2)
		if y6 > 7:
			x = x-9
			x9 = 5+1
			paths.append(3)
		else:
			x9 = x9*x9
			x = 2*x
			x9 = 6*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))