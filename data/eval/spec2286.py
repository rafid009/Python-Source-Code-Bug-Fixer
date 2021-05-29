import numpy as np 

def function(x):

	h4 = 3
	n9 = 1
	paths = []
	try:
		if n9 <= 6:
			x = n9*x
			h4 = h4*9
			paths.append(1)
		else:
			x = x*1
			h4 = h4/2
			paths.append(2)
		if h4 < 9:
			n9 = n9/x
			paths.append(3)
		else:
			n9 = n9-7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))