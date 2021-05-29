import numpy as np 

def function(x):

	i8 = 4
	n8 = x
	paths = []
	try:
		if i8 < 9:
			x = 0*x
			i8 = i8+7
			i8 = x-7
			paths.append(1)
		else:
			n8 = n8*n8
			i8 = 0-i8
			n8 = n8*x
			paths.append(2)
		if x >= 3:
			n8 = n8+3
			i8 = i8-n8
			x = x/i8
			paths.append(3)
		else:
			i8 = i8*x
			x = 0+3
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))