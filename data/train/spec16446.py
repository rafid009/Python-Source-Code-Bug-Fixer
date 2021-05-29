import numpy as np 

def function(x):

	x8 = 9
	b8 = x
	paths = []
	try:
		if x8 < 8:
			b8 = x8+3
			b8 = b8*8
			b8 = 9+x8
			paths.append(1)
		else:
			b8 = 8/b8
			paths.append(2)
		if x >= 9:
			x8 = x8-1
			b8 = b8*7
			paths.append(3)
		else:
			x8 = x8/5
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