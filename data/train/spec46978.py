import numpy as np 

def function(x):

	h2 = x
	n7 = 2
	paths = []
	try:
		if h2 > 2:
			n7 = 6/6
			paths.append(1)
		else:
			n7 = 7*n7
			n7 = h2*7
			x = x*5
			paths.append(2)
		if n7 >= 5:
			h2 = x*h2
			n7 = n7/9
			paths.append(3)
		else:
			h2 = h2/2
			h2 = h2*9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))