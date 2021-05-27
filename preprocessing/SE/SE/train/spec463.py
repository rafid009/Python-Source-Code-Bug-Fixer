import numpy as np 

def function(x):

	b2 = x
	a0 = 4
	x = 4
	paths = []
	try:
		if b2 < 0:
			b2 = b2/5
			paths.append(1)
		else:
			b2 = x+b2
			a0 = x/x
			b2 = 3-9
			paths.append(2)
		if x < 1:
			x = 1/x
			paths.append(3)
		else:
			b2 = 9+b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))