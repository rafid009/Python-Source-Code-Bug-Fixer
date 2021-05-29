import numpy as np 

def function(x):

	y8 = x
	n8 = 9
	x = x
	paths = []
	try:
		if n8 >= 0:
			n8 = 9*5
			y8 = 0-y8
			x = y8+y8
			paths.append(1)
		else:
			n8 = 7+n8
			y8 = y8-3
			y8 = 3+6
			paths.append(2)
		if y8 <= 3:
			y8 = 6-y8
			x = 5+x
			paths.append(3)
		else:
			n8 = n8-8
			y8 = y8+y8
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