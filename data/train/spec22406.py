import numpy as np 

def function(x):

	h6 = 8
	b6 = 6
	paths = []
	try:
		if b6 >= 0:
			x = 0+x
			h6 = 6*7
			paths.append(1)
		else:
			h6 = x+8
			b6 = b6+x
			paths.append(2)
		if h6 > 0:
			b6 = 5-b6
			paths.append(3)
		else:
			x = 1-x
			b6 = 2/b6
			h6 = h6/3
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))