import numpy as np 

def function(x):

	e0 = x
	x6 = x
	paths = []
	try:
		if x >= 5:
			x6 = x+2
			x = x6*x6
			x6 = 2/3
			paths.append(1)
		else:
			x = e0+2
			x = 5-x6
			paths.append(2)
		if x6 < 7:
			x = 6-2
			paths.append(3)
		else:
			x6 = x6*4
			x = x*3
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