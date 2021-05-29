import numpy as np 

def function(x):

	y7 = x
	j8 = 1
	x = 0
	paths = []
	try:
		if j8 <= 0:
			j8 = 1-5
			paths.append(1)
		else:
			y7 = y7/j8
			x = x*y7
			y7 = y7/2
			paths.append(2)
		if x < 0:
			j8 = j8*6
			y7 = y7+1
			y7 = y7+5
			paths.append(3)
		else:
			j8 = 6-j8
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		j8 = y7**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))