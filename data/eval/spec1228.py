import numpy as np 

def function(x):

	e5 = 5
	i8 = 4
	paths = []
	try:
		if x < 4:
			e5 = e5/e5
			x = x-7
			paths.append(1)
		else:
			i8 = i8+7
			paths.append(2)
		if i8 < 1:
			x = 6-x
			x = 3/e5
			paths.append(3)
		else:
			i8 = i8-7
			e5 = 5+e5
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))