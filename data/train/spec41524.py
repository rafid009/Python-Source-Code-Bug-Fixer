import numpy as np 

def function(x):

	h5 = 5
	s8 = x
	paths = []
	try:
		if x < 8:
			x = h5-1
			paths.append(1)
		else:
			s8 = h5/6
			paths.append(2)
		if h5 <= 5:
			s8 = s8+2
			h5 = h5/h5
			x = x+x
			paths.append(3)
		else:
			h5 = h5-s8
			h5 = h5+s8
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		h5 = s8**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))