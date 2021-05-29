import numpy as np 

def function(x):

	a1 = 1
	i8 = 1
	paths = []
	try:
		if i8 > 9:
			x = 4/x
			a1 = 7/1
			a1 = a1+x
			paths.append(1)
		else:
			i8 = i8+6
			a1 = 4+x
			paths.append(2)
		if i8 < 6:
			a1 = a1+a1
			a1 = 1*5
			paths.append(3)
		else:
			i8 = 3+i8
			a1 = x-a1
			i8 = a1+0
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