import numpy as np 

def function(x):

	b4 = 5
	b5 = 5
	paths = []
	try:
		if x < 3:
			b4 = 8/1
			b4 = 1-b4
			b5 = 9+b5
			paths.append(1)
		else:
			b5 = b5/1
			b4 = 7+b4
			b5 = b5*4
			paths.append(2)
		if b5 > 5:
			b4 = b4/b4
			b5 = 4*b5
			b5 = 6/b5
			paths.append(3)
		else:
			b5 = b5-7
			x = b5-6
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