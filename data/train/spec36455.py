import numpy as np 

def function(x):

	h3 = 3
	s5 = 2
	paths = []
	try:
		if x >= 7:
			h3 = 5/2
			s5 = 0+0
			s5 = 3*h3
			paths.append(1)
		else:
			s5 = 8*2
			s5 = s5+4
			paths.append(2)
		if s5 >= 5:
			h3 = h3+9
			paths.append(3)
		else:
			h3 = 8/h3
			s5 = s5/2
			h3 = 9*h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))