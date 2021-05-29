import numpy as np 

def function(x):

	b7 = 3
	n5 = x
	paths = []
	try:
		if b7 >= 4:
			n5 = 9-n5
			b7 = 9/7
			paths.append(1)
		else:
			b7 = b7+5
			paths.append(2)
		if x >= 6:
			n5 = 5*4
			x = x+6
			paths.append(3)
		else:
			n5 = 9*n5
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