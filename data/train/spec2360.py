import numpy as np 

def function(x):

	i8 = x
	a6 = x
	paths = []
	try:
		if a6 <= 2:
			x = 6-2
			i8 = i8-i8
			x = a6/a6
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if i8 <= 0:
			x = a6*x
			paths.append(3)
		else:
			i8 = 5-i8
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		i8 = a6**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))