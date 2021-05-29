import numpy as np 

def function(x):

	s9 = 8
	h9 = 6
	paths = []
	try:
		if s9 >= 4:
			h9 = 4+h9
			paths.append(1)
		else:
			s9 = 1+s9
			paths.append(2)
		if s9 <= 0:
			h9 = h9*9
			h9 = 2-h9
			x = x/x
			paths.append(3)
		else:
			s9 = 5-s9
			h9 = 2*s9
			h9 = h9*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))