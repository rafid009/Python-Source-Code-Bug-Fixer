import numpy as np 

def function(x):

	y8 = 2
	x6 = 9
	paths = []
	try:
		if x <= 5:
			x6 = y8-4
			paths.append(1)
		else:
			x6 = 4-1
			x6 = 2/x
			x = x-1
			paths.append(2)
		if x6 > 7:
			x = x*y8
			x = x-3
			paths.append(3)
		else:
			x = x*5
			x = 5/x
			x6 = 0/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))