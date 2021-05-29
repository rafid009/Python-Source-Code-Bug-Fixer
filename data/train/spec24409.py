import numpy as np 

def function(x):

	x3 = 5
	j8 = x
	paths = []
	try:
		if x < 6:
			j8 = j8*5
			x = 9/x
			j8 = 3/9
			paths.append(1)
		else:
			j8 = 8+j8
			paths.append(2)
		if x3 >= 5:
			x = x-3
			paths.append(3)
		else:
			x = 3/x3
			x3 = 5-j8
			x3 = x3-x3
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