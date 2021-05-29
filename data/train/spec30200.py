import numpy as np 

def function(x):

	y7 = 3
	a4 = 1
	paths = []
	try:
		if x <= 1:
			x = y7-2
			y7 = 7*y7
			x = 6-x
			paths.append(1)
		else:
			a4 = a4*a4
			x = x-y7
			paths.append(2)
		if x < 9:
			a4 = a4*4
			a4 = x+x
			paths.append(3)
		else:
			a4 = a4/7
			a4 = a4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))