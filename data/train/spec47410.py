import numpy as np 

def function(x):

	l1 = x
	h2 = 2
	paths = []
	try:
		if x >= 5:
			x = x+3
			l1 = h2/h2
			l1 = l1-5
			paths.append(1)
		else:
			h2 = 8+l1
			paths.append(2)
		if h2 >= 7:
			x = 7-h2
			x = h2-4
			l1 = l1+h2
			paths.append(3)
		else:
			x = x-x
			l1 = x+2
			h2 = h2-2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))