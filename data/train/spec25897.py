import numpy as np 

def function(x):

	b0 = x
	f1 = 1
	x = x
	paths = []
	try:
		if f1 < 1:
			b0 = 0-6
			x = b0+x
			paths.append(1)
		else:
			b0 = 4*b0
			b0 = 3+b0
			b0 = 2/4
			paths.append(2)
		if f1 < 7:
			x = x/x
			b0 = b0-4
			b0 = b0/5
			paths.append(3)
		else:
			b0 = 4+b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))