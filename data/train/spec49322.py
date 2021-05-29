import numpy as np 

def function(x):

	a8 = x
	y4 = 2
	x = x
	paths = []
	try:
		if x >= 5:
			x = 5*x
			y4 = x-y4
			y4 = y4+2
			paths.append(1)
		else:
			a8 = x*4
			paths.append(2)
		if y4 > 4:
			x = x+4
			paths.append(3)
		else:
			x = x/x
			y4 = 1-3
			a8 = 8/a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))