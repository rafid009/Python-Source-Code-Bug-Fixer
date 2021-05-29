import numpy as np 

def function(x):

	l9 = x
	h9 = x
	paths = []
	try:
		if x >= 8:
			h9 = h9-9
			x = 0-9
			x = x-h9
			paths.append(1)
		else:
			l9 = 9+l9
			x = 9+x
			paths.append(2)
		if h9 > 9:
			x = 2+x
			x = x-2
			paths.append(3)
		else:
			l9 = l9+4
			x = x/l9
			l9 = 5-l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))