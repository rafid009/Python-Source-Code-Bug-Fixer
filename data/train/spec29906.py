import numpy as np 

def function(x):

	x6 = x
	i8 = 2
	x = 7
	paths = []
	try:
		if i8 < 9:
			i8 = x6-i8
			i8 = 1/6
			i8 = 1/2
			paths.append(1)
		else:
			i8 = 6-i8
			i8 = i8/2
			paths.append(2)
		if x6 > 0:
			x = 7*x
			paths.append(3)
		else:
			i8 = i8-i8
			i8 = i8*i8
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))