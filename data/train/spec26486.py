import numpy as np 

def function(x):

	h9 = 9
	l9 = 3
	paths = []
	try:
		if l9 <= 0:
			l9 = l9*l9
			paths.append(1)
		else:
			l9 = x+l9
			x = x-9
			x = x-2
			paths.append(2)
		if h9 <= 4:
			h9 = h9+8
			paths.append(3)
		else:
			h9 = h9+h9
			l9 = 1-5
			x = x+6
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