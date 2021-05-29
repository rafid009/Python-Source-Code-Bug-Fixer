import numpy as np 

def function(x):

	h2 = x
	b3 = x
	x = 3
	paths = []
	try:
		if b3 > 9:
			b3 = 6-b3
			paths.append(1)
		else:
			h2 = 8*1
			paths.append(2)
		if h2 < 5:
			h2 = 3/h2
			paths.append(3)
		else:
			x = 1+b3
			x = x-3
			h2 = 3+h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))