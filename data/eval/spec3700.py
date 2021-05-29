import numpy as np 

def function(x):

	y8 = 1
	j4 = 6
	paths = []
	try:
		if y8 <= 8:
			j4 = y8-9
			paths.append(1)
		else:
			x = 5-5
			x = 8-x
			paths.append(2)
		if x < 3:
			j4 = j4+y8
			paths.append(3)
		else:
			x = x+5
			y8 = 3-y8
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