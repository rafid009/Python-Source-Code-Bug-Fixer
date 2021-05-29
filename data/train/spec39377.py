import numpy as np 

def function(x):

	i8 = x
	n0 = x
	paths = []
	try:
		if i8 > 7:
			x = x+x
			n0 = n0*3
			x = x*i8
			paths.append(1)
		else:
			i8 = 3-i8
			paths.append(2)
		if i8 >= 0:
			i8 = i8/i8
			n0 = 9-x
			paths.append(3)
		else:
			n0 = 8/n0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))