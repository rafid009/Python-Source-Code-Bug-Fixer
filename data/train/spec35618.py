import numpy as np 

def function(x):

	h3 = 5
	b1 = 1
	paths = []
	try:
		if x > 3:
			h3 = h3*h3
			x = h3/6
			x = 7/x
			paths.append(1)
		else:
			b1 = 2-9
			b1 = 7/5
			b1 = h3+b1
			paths.append(2)
		if h3 < 9:
			b1 = b1-8
			paths.append(3)
		else:
			h3 = h3/x
			b1 = h3*x
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		h3 = b1**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))