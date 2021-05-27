import numpy as np 

def function(x):

	q4 = x
	b0 = 0
	paths = []
	try:
		if b0 >= 2:
			x = 8-x
			x = 3+x
			q4 = 4/q4
			paths.append(1)
		else:
			x = 6*x
			b0 = x-9
			paths.append(2)
		if x >= 9:
			x = 6+x
			q4 = q4+x
			paths.append(3)
		else:
			q4 = 4/q4
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