import numpy as np 

def function(x):

	i8 = 4
	j8 = x
	paths = []
	try:
		if j8 > 9:
			j8 = 7+2
			paths.append(1)
		else:
			j8 = j8-6
			i8 = j8-i8
			paths.append(2)
		if i8 > 2:
			i8 = 9+j8
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))