import numpy as np 

def function(x):

	v2 = x
	h3 = 3
	paths = []
	try:
		if x < 6:
			h3 = 0/5
			v2 = 1/v2
			paths.append(1)
		else:
			h3 = h3+8
			h3 = h3-7
			h3 = x-h3
			paths.append(2)
		if v2 <= 7:
			h3 = 3-x
			h3 = h3-x
			h3 = 2*v2
			paths.append(3)
		else:
			x = x/h3
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		h3 = v2**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))