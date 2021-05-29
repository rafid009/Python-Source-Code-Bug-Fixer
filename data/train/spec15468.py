import numpy as np 

def function(x):

	a7 = 5
	x4 = 9
	paths = []
	try:
		if x4 <= 8:
			x4 = a7/7
			x4 = x/3
			x4 = x-x4
			paths.append(1)
		else:
			a7 = a7*7
			x4 = x4-2
			a7 = a7+x4
			paths.append(2)
		if x < 6:
			x = x-6
			a7 = 4-x
			x = x/9
			paths.append(3)
		else:
			a7 = a7/x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))