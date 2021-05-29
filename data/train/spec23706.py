import numpy as np 

def function(x):

	b8 = 0
	b9 = 5
	paths = []
	try:
		if b9 <= 0:
			x = x+b9
			paths.append(1)
		else:
			b9 = x/x
			b9 = b9+b9
			b8 = b8+3
			paths.append(2)
		if b8 >= 2:
			x = x*3
			paths.append(3)
		else:
			x = 8/b9
			b8 = b8/8
			b8 = b8/x
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