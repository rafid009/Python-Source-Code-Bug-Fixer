import numpy as np 

def function(x):

	n3 = x
	x7 = 4
	paths = []
	try:
		if n3 <= 2:
			x = x+5
			n3 = x+9
			paths.append(1)
		else:
			n3 = n3/5
			x7 = x7/5
			paths.append(2)
		if n3 >= 5:
			x = x-9
			x7 = 7-x7
			paths.append(3)
		else:
			x7 = x-x7
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