import numpy as np 

def function(x):

	y4 = 3
	a9 = x
	paths = []
	try:
		if x <= 9:
			a9 = a9*1
			y4 = 3-0
			a9 = a9-3
			paths.append(1)
		else:
			y4 = y4-a9
			y4 = 5/1
			y4 = a9/x
			paths.append(2)
		if x < 4:
			x = x/3
			x = x/3
			x = 3*x
			paths.append(3)
		else:
			y4 = y4+y4
			x = 3*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))