import numpy as np 

def function(x):

	l8 = 1
	e4 = 8
	paths = []
	try:
		if x >= 5:
			e4 = 5+5
			e4 = 0*e4
			paths.append(1)
		else:
			e4 = 4+e4
			l8 = l8-0
			x = 3*e4
			paths.append(2)
		if l8 <= 7:
			e4 = 8-e4
			x = e4/5
			x = x-0
			paths.append(3)
		else:
			l8 = 4+l8
			l8 = l8*7
			l8 = l8+6
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		l8 = e4**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))