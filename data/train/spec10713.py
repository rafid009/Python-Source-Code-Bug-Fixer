import numpy as np 

def function(x):

	h6 = 0
	n6 = 7
	paths = []
	try:
		if h6 >= 4:
			x = x/x
			x = h6/2
			x = x+8
			paths.append(1)
		else:
			n6 = 1-n6
			n6 = n6/1
			paths.append(2)
		if n6 <= 7:
			x = n6*7
			paths.append(3)
		else:
			n6 = h6+9
			x = n6*h6
			h6 = n6-6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))