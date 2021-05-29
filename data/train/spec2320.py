import numpy as np 

def function(x):

	b5 = 6
	h1 = 7
	paths = []
	try:
		if x <= 9:
			b5 = 2*3
			b5 = h1*h1
			h1 = h1-9
			paths.append(1)
		else:
			b5 = 2+5
			b5 = b5+4
			paths.append(2)
		if x <= 0:
			h1 = h1+3
			h1 = h1+h1
			paths.append(3)
		else:
			b5 = b5*6
			x = x/b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))