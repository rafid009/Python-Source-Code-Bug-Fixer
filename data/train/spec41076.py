import numpy as np 

def function(x):

	y1 = x
	e3 = 9
	paths = []
	try:
		if y1 <= 6:
			x = x+7
			x = 1+y1
			e3 = x-1
			paths.append(1)
		else:
			e3 = 4/3
			paths.append(2)
		if x < 9:
			e3 = e3-6
			e3 = 7/e3
			paths.append(3)
		else:
			e3 = e3*2
			e3 = e3/3
			e3 = 0+e3
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