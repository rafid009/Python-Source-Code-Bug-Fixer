import numpy as np 

def function(x):

	l1 = 1
	e2 = x
	paths = []
	try:
		if x > 4:
			e2 = e2+0
			l1 = l1*l1
			paths.append(1)
		else:
			l1 = l1-l1
			paths.append(2)
		if l1 >= 9:
			e2 = e2*x
			x = x-x
			paths.append(3)
		else:
			l1 = 5+l1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))