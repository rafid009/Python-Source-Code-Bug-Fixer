import numpy as np 

def function(x):

	e1 = x
	l9 = 4
	paths = []
	try:
		if l9 > 6:
			e1 = 6*7
			e1 = l9*5
			x = 8/x
			paths.append(1)
		else:
			x = 5-x
			x = l9/x
			e1 = e1-x
			paths.append(2)
		if e1 < 2:
			x = x-x
			e1 = x+e1
			paths.append(3)
		else:
			l9 = l9*8
			l9 = 0*l9
			e1 = x*e1
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