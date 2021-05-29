import numpy as np 

def function(x):

	l5 = x
	e7 = 1
	paths = []
	try:
		if e7 < 9:
			l5 = l5/e7
			x = x+3
			paths.append(1)
		else:
			l5 = l5+8
			e7 = e7+2
			x = 2/x
			paths.append(2)
		if l5 >= 1:
			l5 = l5-l5
			x = x-5
			x = 8*4
			paths.append(3)
		else:
			x = e7/x
			l5 = 2-2
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))