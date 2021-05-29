import numpy as np 

def function(x):

	l6 = 2
	e0 = 1
	paths = []
	try:
		if e0 >= 5:
			x = 5*3
			paths.append(1)
		else:
			l6 = 5/2
			l6 = 4-6
			e0 = e0/2
			paths.append(2)
		if x <= 6:
			l6 = e0*x
			paths.append(3)
		else:
			l6 = l6-7
			l6 = 1-x
			l6 = l6/e0
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))