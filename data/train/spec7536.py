import numpy as np 

def function(x):

	h2 = 2
	k5 = x
	paths = []
	try:
		if x < 1:
			x = 1+k5
			x = x/8
			paths.append(1)
		else:
			h2 = h2+2
			paths.append(2)
		if k5 < 9:
			h2 = 1*4
			x = k5-3
			h2 = h2-9
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		h2 = k5**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))