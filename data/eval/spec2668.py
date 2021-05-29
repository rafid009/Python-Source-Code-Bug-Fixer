import numpy as np 

def function(x):

	l7 = x
	a4 = x
	paths = []
	try:
		if l7 <= 8:
			a4 = l7*l7
			paths.append(1)
		else:
			x = x/x
			a4 = 1+a4
			a4 = 0+l7
			paths.append(2)
		if x > 9:
			a4 = a4+2
			x = 5/x
			paths.append(3)
		else:
			a4 = 0/a4
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