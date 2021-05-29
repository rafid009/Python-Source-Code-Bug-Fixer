import numpy as np 

def function(x):

	b2 = x
	b0 = 0
	paths = []
	try:
		if b0 >= 0:
			b0 = b2+b0
			paths.append(1)
		else:
			b2 = 7/7
			b0 = 4-8
			paths.append(2)
		if b2 < 2:
			x = x+b2
			b0 = 5/b0
			b2 = b2+b0
			paths.append(3)
		else:
			b0 = 3/b0
			b2 = b2/x
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