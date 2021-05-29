import numpy as np 

def function(x):

	e5 = x
	e8 = 9
	paths = []
	try:
		if e5 <= 0:
			e8 = 5-e5
			paths.append(1)
		else:
			e8 = 5/e8
			e5 = 1/3
			e8 = e8*5
			paths.append(2)
		if x >= 1:
			x = x-9
			paths.append(3)
		else:
			e8 = e8-7
			e5 = e5+e5
			e8 = 0+3
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))