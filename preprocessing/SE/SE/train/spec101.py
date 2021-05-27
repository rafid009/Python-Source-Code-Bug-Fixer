import numpy as np 

def function(x):

	b9 = x
	h1 = x
	paths = []
	try:
		if b9 < 3:
			x = x+8
			h1 = x/6
			paths.append(1)
		else:
			x = b9/x
			b9 = 2*9
			x = 2/7
			paths.append(2)
		if b9 < 3:
			b9 = b9*2
			paths.append(3)
		else:
			b9 = b9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))