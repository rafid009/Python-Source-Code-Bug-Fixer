import numpy as np 

def function(x):

	l2 = x
	j7 = 9
	paths = []
	try:
		if l2 > 5:
			l2 = x-5
			paths.append(1)
		else:
			j7 = l2*4
			paths.append(2)
		if l2 >= 1:
			x = 3/x
			paths.append(3)
		else:
			x = x+6
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