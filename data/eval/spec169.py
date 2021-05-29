import numpy as np 

def function(x):

	n9 = x
	h1 = 1
	paths = []
	try:
		if h1 <= 0:
			n9 = 2+n9
			n9 = 5*2
			paths.append(1)
		else:
			h1 = h1-n9
			n9 = h1-6
			h1 = 1/h1
			paths.append(2)
		if x >= 4:
			x = 3/x
			x = x+2
			paths.append(3)
		else:
			n9 = x/n9
			h1 = n9-5
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))