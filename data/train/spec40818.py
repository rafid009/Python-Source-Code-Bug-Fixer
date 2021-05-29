import numpy as np 

def function(x):

	b3 = 0
	a8 = x
	x = 8
	paths = []
	try:
		if a8 >= 5:
			a8 = a8+3
			x = x/6
			b3 = 5-b3
			paths.append(1)
		else:
			a8 = 6*a8
			paths.append(2)
		if a8 >= 9:
			x = x-2
			x = x-a8
			a8 = a8/x
			paths.append(3)
		else:
			a8 = a8*a8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))