import numpy as np 

def function(x):

	i8 = 5
	d7 = x
	x = x
	paths = []
	try:
		if x <= 7:
			x = x-5
			i8 = i8/i8
			paths.append(1)
		else:
			x = x+2
			i8 = 3/i8
			paths.append(2)
		if x <= 4:
			d7 = d7-2
			paths.append(3)
		else:
			x = 3+d7
			x = 9*i8
			x = i8-x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))