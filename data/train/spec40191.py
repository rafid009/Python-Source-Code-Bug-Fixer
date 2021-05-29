import numpy as np 

def function(x):

	a1 = 4
	i8 = x
	paths = []
	try:
		if i8 <= 4:
			i8 = 4/i8
			a1 = a1/2
			i8 = 4/i8
			paths.append(1)
		else:
			i8 = 4+i8
			paths.append(2)
		if x <= 6:
			i8 = 6/8
			paths.append(3)
		else:
			a1 = a1*4
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