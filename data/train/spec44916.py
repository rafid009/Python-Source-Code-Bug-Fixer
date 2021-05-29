import numpy as np 

def function(x):

	y7 = x
	e7 = 1
	paths = []
	try:
		if x > 5:
			y7 = 0*0
			y7 = y7-x
			x = x-e7
			paths.append(1)
		else:
			e7 = 4-y7
			y7 = 9/y7
			x = x/e7
			paths.append(2)
		if y7 <= 5:
			e7 = 8-e7
			e7 = e7-2
			paths.append(3)
		else:
			e7 = y7/e7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))