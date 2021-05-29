import numpy as np 

def function(x):

	b4 = x
	h8 = 2
	x = 5
	paths = []
	try:
		if h8 > 2:
			h8 = 4-4
			x = x+1
			paths.append(1)
		else:
			x = 7-x
			x = 3+x
			paths.append(2)
		if h8 > 7:
			b4 = 8+b4
			h8 = 1-b4
			paths.append(3)
		else:
			x = x-6
			x = x/2
			b4 = b4/3
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))