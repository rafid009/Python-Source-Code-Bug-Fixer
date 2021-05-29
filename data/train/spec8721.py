import numpy as np 

def function(x):

	x9 = 0
	e8 = 4
	paths = []
	try:
		if x <= 6:
			x = x-0
			e8 = e8+2
			paths.append(1)
		else:
			x9 = 0*3
			paths.append(2)
		if x9 <= 5:
			x9 = 9/6
			x = 3*x
			e8 = 0*1
			paths.append(3)
		else:
			x = x/e8
			x9 = e8-x9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))