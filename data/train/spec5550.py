import numpy as np 

def function(x):

	h8 = 7
	s1 = 1
	paths = []
	try:
		if x >= 6:
			h8 = h8-5
			h8 = h8-4
			paths.append(1)
		else:
			x = x*h8
			h8 = h8-3
			paths.append(2)
		if h8 >= 0:
			s1 = s1/s1
			s1 = 4/s1
			paths.append(3)
		else:
			h8 = h8+1
			x = 7*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))