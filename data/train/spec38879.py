import numpy as np 

def function(x):

	h5 = x
	s9 = x
	x = x
	paths = []
	try:
		if h5 > 5:
			s9 = 3/x
			paths.append(1)
		else:
			h5 = x/7
			h5 = h5-5
			h5 = 0+h5
			paths.append(2)
		if h5 < 3:
			x = 5+5
			x = x-1
			x = 8-x
			paths.append(3)
		else:
			h5 = h5-8
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))