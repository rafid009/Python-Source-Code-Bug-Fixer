import numpy as np 

def function(x):

	y5 = x
	j8 = x
	paths = []
	try:
		if j8 <= 7:
			j8 = j8/y5
			paths.append(1)
		else:
			j8 = j8/j8
			x = x/x
			paths.append(2)
		if j8 < 7:
			x = y5*3
			paths.append(3)
		else:
			j8 = x+8
			j8 = j8/j8
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))