import numpy as np 

def function(x):

	k5 = x
	b6 = x
	paths = []
	try:
		if b6 > 8:
			b6 = b6*8
			paths.append(1)
		else:
			b6 = x-8
			paths.append(2)
		if x >= 7:
			k5 = x/4
			paths.append(3)
		else:
			x = b6/x
			x = 4*5
			x = b6/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))