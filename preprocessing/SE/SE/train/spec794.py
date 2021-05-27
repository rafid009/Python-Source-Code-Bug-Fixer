import numpy as np 

def function(x):

	b0 = 6
	b2 = x
	x = x
	paths = []
	try:
		if b0 < 9:
			b0 = 7-b0
			paths.append(1)
		else:
			b0 = b2-b2
			paths.append(2)
		if b0 <= 2:
			b2 = 3+9
			paths.append(3)
		else:
			b0 = 9-b0
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