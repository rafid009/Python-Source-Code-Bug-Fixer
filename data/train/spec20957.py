import numpy as np 

def function(x):

	y4 = 2
	a7 = 4
	paths = []
	try:
		if a7 > 4:
			x = 5*y4
			a7 = 8+a7
			x = y4/x
			paths.append(1)
		else:
			a7 = 8/3
			paths.append(2)
		if y4 <= 2:
			y4 = 0+9
			x = 0-9
			a7 = a7*6
			paths.append(3)
		else:
			y4 = 4-y4
			x = a7*7
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