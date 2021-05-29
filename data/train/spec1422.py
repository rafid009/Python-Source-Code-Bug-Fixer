import numpy as np 

def function(x):

	h4 = x
	n4 = 0
	paths = []
	try:
		if x <= 2:
			x = h4*8
			x = x*6
			paths.append(1)
		else:
			h4 = h4/9
			x = x*n4
			h4 = 3*h4
			paths.append(2)
		if h4 > 7:
			x = 7*9
			n4 = 9/3
			paths.append(3)
		else:
			n4 = h4*9
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))