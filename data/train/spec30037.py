import numpy as np 

def function(x):

	i8 = x
	i1 = 6
	paths = []
	try:
		if i1 >= 9:
			i1 = x-i1
			paths.append(1)
		else:
			i1 = 9/i1
			i8 = 8+i8
			i1 = 0-i1
			paths.append(2)
		if i1 >= 6:
			i1 = 9*i1
			i1 = i1*x
			x = 8/9
			paths.append(3)
		else:
			i8 = 9+x
			i1 = i8/6
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