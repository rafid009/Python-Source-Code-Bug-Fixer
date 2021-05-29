import numpy as np 

def function(x):

	x9 = x
	b4 = 8
	paths = []
	try:
		if x <= 2:
			b4 = 3+2
			x = x9-3
			paths.append(1)
		else:
			x9 = 5/3
			paths.append(2)
		if b4 >= 7:
			x = 1*x9
			x = 8+x9
			x = x9*x
			paths.append(3)
		else:
			b4 = b4*4
			b4 = x9-b4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))