import numpy as np 

def function(x):

	b8 = x
	e8 = 0
	paths = []
	try:
		if e8 > 4:
			b8 = 1-0
			b8 = 6*x
			e8 = e8/1
			paths.append(1)
		else:
			b8 = b8*3
			paths.append(2)
		if e8 > 0:
			b8 = b8/3
			e8 = x-3
			paths.append(3)
		else:
			e8 = b8-e8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))