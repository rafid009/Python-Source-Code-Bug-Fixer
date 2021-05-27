import numpy as np 

def function(x):

	y6 = x
	j7 = x
	x = 8
	paths = []
	try:
		if j7 >= 6:
			y6 = y6-7
			paths.append(1)
		else:
			j7 = 9+j7
			paths.append(2)
		if x > 8:
			y6 = 8+6
			y6 = y6+9
			paths.append(3)
		else:
			y6 = 0+y6
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))