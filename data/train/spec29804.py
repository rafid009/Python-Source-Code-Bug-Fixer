import numpy as np 

def function(x):

	h3 = x
	b8 = x
	paths = []
	try:
		if h3 < 2:
			b8 = b8*7
			paths.append(1)
		else:
			x = x-7
			x = 3/x
			b8 = b8/2
			paths.append(2)
		if b8 > 0:
			b8 = b8*1
			x = 7*x
			x = x+1
			paths.append(3)
		else:
			h3 = b8*1
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))