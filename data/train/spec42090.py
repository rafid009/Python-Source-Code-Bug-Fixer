import numpy as np 

def function(x):

	h6 = 7
	n2 = x
	paths = []
	try:
		if x <= 9:
			h6 = h6/2
			n2 = 1+x
			h6 = h6-n2
			paths.append(1)
		else:
			h6 = h6/8
			x = x+2
			h6 = 5+h6
			paths.append(2)
		if x >= 4:
			n2 = n2-0
			paths.append(3)
		else:
			n2 = 1/n2
			h6 = h6*n2
			n2 = n2-n2
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))