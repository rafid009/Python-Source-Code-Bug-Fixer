import numpy as np 

def function(x):

	b7 = x
	s9 = 1
	paths = []
	try:
		if b7 >= 4:
			b7 = b7*b7
			paths.append(1)
		else:
			b7 = x-0
			x = 4*x
			paths.append(2)
		if b7 > 4:
			b7 = b7-0
			paths.append(3)
		else:
			b7 = b7-8
			b7 = b7/9
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