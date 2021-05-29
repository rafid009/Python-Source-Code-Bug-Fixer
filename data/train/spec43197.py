import numpy as np 

def function(x):

	b2 = 4
	o9 = 2
	paths = []
	try:
		if x < 1:
			b2 = o9/2
			paths.append(1)
		else:
			o9 = o9+8
			paths.append(2)
		if x < 3:
			b2 = b2*x
			paths.append(3)
		else:
			b2 = 7+b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))