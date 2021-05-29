import numpy as np 

def function(x):

	j8 = 9
	y2 = x
	x = x
	paths = []
	try:
		if x > 9:
			j8 = j8-x
			paths.append(1)
		else:
			j8 = j8/j8
			j8 = 4-j8
			paths.append(2)
		if y2 > 8:
			j8 = 1*6
			y2 = 3-x
			paths.append(3)
		else:
			x = x-0
			x = x/7
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