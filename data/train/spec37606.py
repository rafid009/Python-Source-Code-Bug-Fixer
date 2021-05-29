import numpy as np 

def function(x):

	s7 = x
	h3 = 3
	paths = []
	try:
		if x > 1:
			x = x*8
			x = 2+7
			h3 = 3-h3
			paths.append(1)
		else:
			x = x-0
			h3 = h3/s7
			paths.append(2)
		if s7 >= 2:
			x = s7*x
			paths.append(3)
		else:
			s7 = x/2
			h3 = h3-7
			h3 = h3-2
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		s7 = h3**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))