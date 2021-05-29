import numpy as np 

def function(x):

	e3 = x
	y6 = 6
	paths = []
	try:
		if y6 >= 7:
			y6 = e3/y6
			y6 = 9-y6
			x = 2+2
			paths.append(1)
		else:
			e3 = e3+9
			paths.append(2)
		if x >= 1:
			y6 = x+7
			paths.append(3)
		else:
			x = x-7
			y6 = y6-0
			x = x-6
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))