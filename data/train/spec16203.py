import numpy as np 

def function(x):

	b8 = 7
	paths = []
	try:
		if b8 <= 7:
			b8 = 5*b8
			paths.append(1)
		else:
			b8 = 0/b8
			b8 = b8*b8
			paths.append(2)
		if x > 8:
			b8 = 4/b8
			paths.append(3)
		else:
			x = x+x
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