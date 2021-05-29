import numpy as np 

def function(x):

	h2 = 3
	k7 = x
	paths = []
	try:
		if x > 9:
			k7 = x+k7
			h2 = k7*h2
			paths.append(1)
		else:
			x = 6/x
			h2 = 1-h2
			paths.append(2)
		if k7 >= 3:
			x = 1/8
			k7 = 0+2
			k7 = h2+k7
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))