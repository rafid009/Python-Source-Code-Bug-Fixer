import numpy as np 

def function(x):

	y7 = x
	j4 = x
	paths = []
	try:
		if j4 >= 3:
			j4 = j4+j4
			j4 = j4*y7
			paths.append(1)
		else:
			j4 = 3/y7
			x = x*1
			paths.append(2)
		if j4 >= 5:
			y7 = y7+0
			y7 = x/y7
			y7 = y7+y7
			paths.append(3)
		else:
			j4 = j4-1
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))