import numpy as np 

def function(x):

	b5 = x
	b8 = 3
	paths = []
	try:
		if b8 <= 1:
			b5 = 2*9
			paths.append(1)
		else:
			x = 0-x
			b8 = b5+x
			paths.append(2)
		if b8 > 0:
			b5 = x/x
			paths.append(3)
		else:
			b8 = 1-b8
			b5 = 5/b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))