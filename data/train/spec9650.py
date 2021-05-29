import numpy as np 

def function(x):

	a8 = x
	x4 = x
	paths = []
	try:
		if a8 <= 2:
			x = x-6
			paths.append(1)
		else:
			a8 = a8+7
			a8 = a8+9
			paths.append(2)
		if x <= 7:
			x = a8/x4
			a8 = 9/a8
			a8 = a8+a8
			paths.append(3)
		else:
			x4 = 2*3
			x = x+5
			x4 = x4-5
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		a8 = x4**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))