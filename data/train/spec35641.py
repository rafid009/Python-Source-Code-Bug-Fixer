import numpy as np 

def function(x):

	j2 = 5
	y7 = x
	paths = []
	try:
		if j2 < 5:
			y7 = j2/8
			paths.append(1)
		else:
			x = 7/y7
			paths.append(2)
		if j2 <= 7:
			j2 = x-2
			y7 = 1*9
			paths.append(3)
		else:
			y7 = j2/y7
			y7 = y7/y7
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))