import numpy as np 

def function(x):

	k2 = 0
	h6 = x
	x = 8
	paths = []
	try:
		if k2 < 7:
			x = x+x
			h6 = h6/3
			h6 = h6/2
			paths.append(1)
		else:
			h6 = k2/8
			k2 = x*k2
			paths.append(2)
		if k2 < 9:
			k2 = k2+k2
			paths.append(3)
		else:
			h6 = x*5
			x = x/h6
			h6 = 9/3
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