import numpy as np 

def function(x):

	n6 = x
	h9 = 0
	paths = []
	try:
		if h9 >= 3:
			n6 = 0+0
			n6 = n6/n6
			x = x*4
			paths.append(1)
		else:
			n6 = 6+n6
			x = 6*7
			paths.append(2)
		if x < 4:
			x = x/h9
			paths.append(3)
		else:
			h9 = h9+2
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))