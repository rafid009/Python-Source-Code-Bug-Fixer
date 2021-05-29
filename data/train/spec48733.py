import numpy as np 

def function(x):

	l4 = 4
	e7 = x
	paths = []
	try:
		if l4 < 6:
			e7 = 6/e7
			l4 = l4+5
			e7 = 4+e7
			paths.append(1)
		else:
			x = x+e7
			x = x-x
			paths.append(2)
		if l4 <= 2:
			e7 = 9+e7
			l4 = e7+l4
			paths.append(3)
		else:
			x = x*1
			e7 = e7/8
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))