import numpy as np 

def function(x):

	y7 = x
	e6 = x
	paths = []
	try:
		if y7 >= 4:
			x = x*3
			x = x*8
			paths.append(1)
		else:
			e6 = e6+y7
			paths.append(2)
		if e6 <= 9:
			y7 = y7/y7
			x = x+7
			paths.append(3)
		else:
			e6 = e6-e6
			y7 = x-e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))