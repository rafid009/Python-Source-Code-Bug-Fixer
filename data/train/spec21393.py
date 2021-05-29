import numpy as np 

def function(x):

	l1 = x
	e6 = x
	paths = []
	try:
		if x >= 4:
			x = x+x
			e6 = 7/e6
			paths.append(1)
		else:
			l1 = 2+2
			l1 = x*x
			paths.append(2)
		if e6 > 3:
			x = x/l1
			l1 = 6-9
			paths.append(3)
		else:
			x = x-1
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