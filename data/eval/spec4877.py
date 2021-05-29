import numpy as np 

def function(x):

	e8 = 3
	l2 = x
	paths = []
	try:
		if l2 < 8:
			x = e8-x
			x = x*x
			paths.append(1)
		else:
			l2 = 7*l2
			e8 = e8+4
			e8 = e8-9
			paths.append(2)
		if e8 >= 8:
			l2 = l2-9
			x = 6/x
			paths.append(3)
		else:
			e8 = 7/e8
			l2 = l2/4
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		e8 = l2**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))