import numpy as np 

def function(x):

	h1 = x
	s6 = x
	paths = []
	try:
		if x >= 5:
			s6 = s6*x
			h1 = h1/h1
			h1 = h1/x
			paths.append(1)
		else:
			s6 = s6+x
			h1 = h1/h1
			x = x*9
			paths.append(2)
		if s6 >= 4:
			x = x*4
			paths.append(3)
		else:
			x = s6*1
			h1 = h1-8
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))