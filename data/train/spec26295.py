import numpy as np 

def function(x):

	h3 = x
	n9 = x
	paths = []
	try:
		if x < 7:
			h3 = h3-5
			h3 = h3/3
			paths.append(1)
		else:
			h3 = 0+h3
			x = x*4
			x = n9-7
			paths.append(2)
		if n9 < 8:
			n9 = n9-6
			x = x/x
			paths.append(3)
		else:
			x = n9/3
			x = 0-x
			n9 = n9+n9
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		n9 = h3**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))