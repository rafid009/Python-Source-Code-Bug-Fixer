import numpy as np 

def function(x):

	e0 = 8
	l6 = x
	paths = []
	try:
		if e0 <= 4:
			x = x+5
			x = x-7
			paths.append(1)
		else:
			e0 = e0/2
			l6 = l6+6
			e0 = 9-l6
			paths.append(2)
		if x < 6:
			l6 = l6+8
			paths.append(3)
		else:
			e0 = 4*e0
			e0 = e0/e0
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		e0 = l6**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))