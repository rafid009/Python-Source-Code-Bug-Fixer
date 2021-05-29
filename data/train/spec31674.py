import numpy as np 

def function(x):

	h6 = x
	x2 = x
	x = 6
	paths = []
	try:
		if x2 > 1:
			x = h6+2
			x2 = x2/1
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if x2 <= 7:
			x2 = x2+5
			x = x*5
			h6 = 3+x2
			paths.append(3)
		else:
			x = 1+x2
			x2 = 3-1
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		h6 = x2**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))