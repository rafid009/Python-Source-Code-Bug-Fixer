import numpy as np 

def function(x):

	l1 = x
	b0 = x
	paths = []
	try:
		if l1 > 8:
			b0 = 9+x
			b0 = b0-4
			paths.append(1)
		else:
			x = 2-x
			l1 = b0/l1
			b0 = x-b0
			paths.append(2)
		if b0 >= 0:
			l1 = l1+b0
			b0 = l1-5
			paths.append(3)
		else:
			b0 = 8-b0
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