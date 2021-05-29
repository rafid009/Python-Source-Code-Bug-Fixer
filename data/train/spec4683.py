import numpy as np 

def function(x):

	b4 = x
	paths = []
	try:
		if b4 > 9:
			b4 = 5+b4
			paths.append(1)
		else:
			x = x-2
			b4 = 4*b4
			paths.append(2)
		if b4 <= 1:
			x = 9+b4
			paths.append(3)
		else:
			b4 = b4+3
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))