import numpy as np 

def function(x):

	h1 = 7
	b0 = x
	paths = []
	try:
		if x < 2:
			x = x+3
			x = 3*5
			paths.append(1)
		else:
			b0 = b0+3
			x = h1+b0
			paths.append(2)
		if x <= 1:
			x = 1-x
			x = b0-3
			b0 = 2-b0
			paths.append(3)
		else:
			x = x*8
			x = 1-h1
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))