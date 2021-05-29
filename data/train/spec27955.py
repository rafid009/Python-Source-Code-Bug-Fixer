import numpy as np 

def function(x):

	i8 = 2
	p8 = 8
	paths = []
	try:
		if x < 5:
			p8 = 1/p8
			paths.append(1)
		else:
			p8 = p8/2
			paths.append(2)
		if i8 >= 7:
			p8 = 3*5
			paths.append(3)
		else:
			x = i8-x
			i8 = i8/4
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