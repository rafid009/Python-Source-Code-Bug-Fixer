import numpy as np 

def function(x):

	y6 = x
	m0 = 1
	paths = []
	try:
		if y6 > 2:
			x = 7*7
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if y6 > 4:
			x = x-8
			m0 = 5-m0
			paths.append(3)
		else:
			y6 = 8/6
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