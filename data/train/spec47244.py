import numpy as np 

def function(x):

	j8 = x
	y1 = 3
	paths = []
	try:
		if y1 <= 0:
			y1 = j8+y1
			y1 = y1*4
			x = 8-x
			paths.append(1)
		else:
			j8 = 7-y1
			y1 = x/y1
			j8 = j8-y1
			paths.append(2)
		if x >= 2:
			j8 = j8/y1
			y1 = y1-2
			paths.append(3)
		else:
			y1 = 0-9
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))