import numpy as np 

def function(x):

	l9 = x
	y7 = x
	paths = []
	try:
		if y7 >= 7:
			x = 2*6
			y7 = 8*y7
			paths.append(1)
		else:
			y7 = x-5
			y7 = y7-x
			paths.append(2)
		if x <= 3:
			x = x+x
			paths.append(3)
		else:
			l9 = 4*y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))