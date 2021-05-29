import numpy as np 

def function(x):

	h0 = x
	b9 = 1
	paths = []
	try:
		if b9 > 2:
			b9 = x+4
			paths.append(1)
		else:
			b9 = b9*3
			b9 = 7+7
			b9 = 7*1
			paths.append(2)
		if x >= 4:
			h0 = h0*b9
			b9 = 7-b9
			paths.append(3)
		else:
			b9 = h0-8
			x = 3/x
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