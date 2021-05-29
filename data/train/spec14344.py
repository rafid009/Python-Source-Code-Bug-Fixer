import numpy as np 

def function(x):

	y1 = 3
	a3 = x
	paths = []
	try:
		if y1 < 8:
			x = x+y1
			paths.append(1)
		else:
			x = y1+7
			paths.append(2)
		if a3 <= 7:
			y1 = y1*y1
			a3 = a3/y1
			paths.append(3)
		else:
			x = x-6
			a3 = 0-y1
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))