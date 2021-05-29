import numpy as np 

def function(x):

	y2 = 5
	j8 = x
	paths = []
	try:
		if y2 <= 7:
			y2 = 9/y2
			y2 = 5+y2
			paths.append(1)
		else:
			x = j8/x
			y2 = x-3
			paths.append(2)
		if x <= 4:
			j8 = j8-4
			paths.append(3)
		else:
			j8 = 3-y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))