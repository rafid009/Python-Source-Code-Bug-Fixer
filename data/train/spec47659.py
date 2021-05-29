import numpy as np 

def function(x):

	l4 = x
	f1 = 6
	paths = []
	try:
		if f1 <= 1:
			x = x+f1
			x = x/x
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if f1 >= 6:
			x = x/2
			paths.append(3)
		else:
			x = 3/x
			l4 = l4-2
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