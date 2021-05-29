import numpy as np 

def function(x):

	x7 = 2
	j9 = 4
	paths = []
	try:
		if x >= 0:
			x7 = x7-x7
			x = x-1
			paths.append(1)
		else:
			x7 = x7+8
			x = 3/4
			x7 = x7-x7
			paths.append(2)
		if x < 3:
			x7 = x7*7
			x7 = x7/7
			paths.append(3)
		else:
			x7 = 8+x7
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))