import numpy as np 

def function(x):

	b1 = 1
	b5 = 0
	paths = []
	try:
		if b1 >= 1:
			x = x+7
			b1 = 3+x
			b1 = b5/2
			paths.append(1)
		else:
			b1 = b1/b1
			b5 = b5-b5
			paths.append(2)
		if b5 > 2:
			b5 = b5*b5
			b1 = b1-b5
			paths.append(3)
		else:
			b5 = 1+b1
			b5 = b5/b5
			x = x+8
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