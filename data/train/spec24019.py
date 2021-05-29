import numpy as np 

def function(x):

	b7 = 4
	h1 = x
	paths = []
	try:
		if x <= 7:
			b7 = 4*b7
			b7 = b7/h1
			x = x/5
			paths.append(1)
		else:
			h1 = 7-x
			b7 = b7-3
			b7 = 4-8
			paths.append(2)
		if b7 <= 4:
			x = x+b7
			paths.append(3)
		else:
			b7 = b7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))