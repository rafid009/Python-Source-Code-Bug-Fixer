import numpy as np 

def function(x):

	l1 = x
	a6 = 2
	paths = []
	try:
		if a6 >= 6:
			a6 = l1+a6
			x = 3/x
			a6 = a6*6
			paths.append(1)
		else:
			a6 = x*a6
			x = 9/x
			paths.append(2)
		if l1 > 0:
			a6 = a6/8
			x = x-0
			paths.append(3)
		else:
			a6 = 6*a6
			x = x*x
			l1 = l1-6
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))