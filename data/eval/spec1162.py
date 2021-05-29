import numpy as np 

def function(x):

	x0 = x
	b2 = 8
	paths = []
	try:
		if x0 < 5:
			x = 8*b2
			b2 = 0/x
			paths.append(1)
		else:
			b2 = b2-8
			b2 = b2-x0
			x = 4+x
			paths.append(2)
		if x >= 8:
			x = x+x
			b2 = x/x
			paths.append(3)
		else:
			x0 = 7+b2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))