import numpy as np 

def function(x):

	x6 = 3
	i8 = 7
	paths = []
	try:
		if x >= 9:
			x6 = i8/x
			x6 = i8/8
			paths.append(1)
		else:
			x = x*i8
			i8 = x6-1
			x6 = 3*x
			paths.append(2)
		if x6 < 9:
			i8 = i8+9
			i8 = 5+i8
			paths.append(3)
		else:
			x = i8-7
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		i8 = x6**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))