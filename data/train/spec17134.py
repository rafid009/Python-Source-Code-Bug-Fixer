import numpy as np 

def function(x):

	y8 = 1
	j0 = 7
	paths = []
	try:
		if y8 > 9:
			x = 2-7
			paths.append(1)
		else:
			x = x*5
			y8 = y8-8
			paths.append(2)
		if x < 5:
			y8 = 7-y8
			y8 = 5-9
			paths.append(3)
		else:
			j0 = j0/4
			j0 = j0*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))