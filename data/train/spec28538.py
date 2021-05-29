import numpy as np 

def function(x):

	n7 = 1
	h2 = x
	paths = []
	try:
		if x > 2:
			h2 = h2/n7
			x = x/2
			n7 = 7/n7
			paths.append(1)
		else:
			h2 = 5-5
			h2 = h2-9
			paths.append(2)
		if x >= 5:
			h2 = n7+4
			x = 0/6
			paths.append(3)
		else:
			h2 = h2+2
			n7 = 5-n7
			n7 = n7/4
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