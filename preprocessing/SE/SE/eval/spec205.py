import numpy as np 

def function(x):

	y7 = x
	e8 = 3
	paths = []
	try:
		if e8 < 6:
			y7 = 5*y7
			paths.append(1)
		else:
			y7 = y7*4
			paths.append(2)
		if y7 < 9:
			e8 = 1*y7
			paths.append(3)
		else:
			e8 = 3+7
			y7 = x+y7
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))