import numpy as np 

def function(x):

	a1 = x
	i8 = 3
	paths = []
	try:
		if a1 <= 1:
			a1 = x/a1
			a1 = a1/6
			paths.append(1)
		else:
			a1 = 0-a1
			x = 1*5
			paths.append(2)
		if x >= 0:
			i8 = 7/i8
			a1 = a1/8
			paths.append(3)
		else:
			i8 = a1*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))