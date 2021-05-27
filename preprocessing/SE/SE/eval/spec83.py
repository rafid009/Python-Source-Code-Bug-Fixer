import numpy as np 

def function(x):

	h9 = x
	n7 = x
	paths = []
	try:
		if h9 < 4:
			x = 4/9
			paths.append(1)
		else:
			n7 = x+0
			h9 = 1/7
			paths.append(2)
		if n7 >= 0:
			n7 = n7-h9
			x = x-5
			h9 = 4*x
			paths.append(3)
		else:
			h9 = h9/9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		n7 = h9**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))