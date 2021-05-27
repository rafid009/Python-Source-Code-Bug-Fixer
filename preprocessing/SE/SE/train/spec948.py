import numpy as np 

def function(x):

	h6 = x
	k0 = x
	paths = []
	try:
		if x <= 3:
			k0 = 6-k0
			paths.append(1)
		else:
			h6 = h6/x
			paths.append(2)
		if x > 8:
			h6 = 0+1
			k0 = 6+x
			x = x*2
			paths.append(3)
		else:
			x = x*9
			k0 = k0-7
			h6 = h6-h6
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		h6 = k0**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))