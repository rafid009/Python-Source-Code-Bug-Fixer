import numpy as np 

def function(x):

	k5 = 1
	b2 = x
	paths = []
	try:
		if x >= 9:
			x = 8*x
			x = 0-3
			paths.append(1)
		else:
			b2 = b2/k5
			k5 = 3/6
			paths.append(2)
		if b2 > 9:
			b2 = b2+3
			b2 = 1+b2
			x = 0+x
			paths.append(3)
		else:
			x = 4+x
			x = 3-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))