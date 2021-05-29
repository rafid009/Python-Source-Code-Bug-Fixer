import numpy as np 

def function(x):

	a8 = 2
	a9 = x
	paths = []
	try:
		if a9 < 8:
			a8 = 9-a8
			x = x*7
			x = x*9
			paths.append(1)
		else:
			a8 = a8-3
			paths.append(2)
		if x > 9:
			a9 = a9/a9
			paths.append(3)
		else:
			x = 3+a8
			a9 = 1+5
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))