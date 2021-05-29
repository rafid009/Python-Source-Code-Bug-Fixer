import numpy as np 

def function(x):

	x2 = x
	l7 = 7
	paths = []
	try:
		if l7 >= 3:
			l7 = l7-6
			paths.append(1)
		else:
			x = x*2
			l7 = 9/8
			paths.append(2)
		if x2 >= 1:
			x = x*x
			x = 0/x
			x2 = 4-x2
			paths.append(3)
		else:
			l7 = 8-l7
			l7 = 4+l7
			l7 = l7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))