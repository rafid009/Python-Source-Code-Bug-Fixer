import numpy as np 

def function(x):

	y6 = x
	x6 = x
	paths = []
	try:
		if x >= 7:
			y6 = 0-y6
			y6 = y6+5
			y6 = y6+x
			paths.append(1)
		else:
			y6 = x+y6
			paths.append(2)
		if x >= 1:
			x6 = x6*7
			x = x+0
			x = x/x
			paths.append(3)
		else:
			x6 = x6+9
			x = 6/x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))