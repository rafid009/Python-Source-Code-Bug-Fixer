import numpy as np 

def function(x):

	f7 = 2
	h8 = x
	paths = []
	try:
		if h8 < 2:
			x = x*f7
			f7 = x*8
			h8 = 5+8
			paths.append(1)
		else:
			f7 = 3/h8
			f7 = 0*f7
			paths.append(2)
		if h8 <= 0:
			h8 = h8+f7
			paths.append(3)
		else:
			f7 = f7/7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		h8 = f7**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))