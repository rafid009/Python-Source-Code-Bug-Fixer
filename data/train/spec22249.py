import numpy as np 

def function(x):

	i8 = 7
	q6 = x
	paths = []
	try:
		if x >= 8:
			q6 = 7*i8
			q6 = 9/q6
			paths.append(1)
		else:
			i8 = 8-9
			x = x+x
			paths.append(2)
		if x >= 3:
			i8 = i8-q6
			q6 = 0/q6
			paths.append(3)
		else:
			i8 = i8*i8
			i8 = i8-x
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