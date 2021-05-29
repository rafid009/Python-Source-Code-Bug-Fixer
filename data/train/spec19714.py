import numpy as np 

def function(x):

	f0 = x
	b2 = x
	paths = []
	try:
		if x >= 2:
			b2 = b2-6
			x = x-7
			b2 = b2-4
			paths.append(1)
		else:
			b2 = 3*6
			paths.append(2)
		if f0 <= 4:
			b2 = b2-6
			paths.append(3)
		else:
			x = 1/x
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