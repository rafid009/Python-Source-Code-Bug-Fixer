import numpy as np 

def function(x):

	y1 = 4
	j9 = 3
	paths = []
	try:
		if x <= 0:
			j9 = x-x
			j9 = 6/x
			paths.append(1)
		else:
			j9 = j9-j9
			paths.append(2)
		if y1 > 1:
			y1 = y1*j9
			paths.append(3)
		else:
			j9 = 7*3
			y1 = 8+y1
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