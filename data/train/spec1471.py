import numpy as np 

def function(x):

	l4 = 2
	r6 = x
	paths = []
	try:
		if x <= 5:
			l4 = l4/x
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if x < 8:
			x = x/4
			l4 = l4+3
			l4 = l4+r6
			paths.append(3)
		else:
			x = 6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))