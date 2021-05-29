import numpy as np 

def function(x):

	w9 = 2
	h3 = x
	x = x
	paths = []
	try:
		if w9 >= 1:
			h3 = x-w9
			paths.append(1)
		else:
			h3 = 6+6
			h3 = h3+4
			x = w9+x
			paths.append(2)
		if x > 4:
			x = x*6
			paths.append(3)
		else:
			x = x-2
			w9 = h3*w9
			x = 6/7
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))