import numpy as np 

def function(x):

	n4 = 1
	h4 = x
	x = 8
	paths = []
	try:
		if h4 < 0:
			x = x-9
			paths.append(1)
		else:
			n4 = n4/h4
			paths.append(2)
		if h4 <= 9:
			x = x/2
			n4 = 0/n4
			x = x/1
			paths.append(3)
		else:
			n4 = 8+n4
			h4 = 7/h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		n4 = h4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))