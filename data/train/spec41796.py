import numpy as np 

def function(x):

	s6 = 2
	h6 = x
	x = x
	paths = []
	try:
		if h6 > 2:
			h6 = 0/h6
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if x > 5:
			h6 = 2+9
			paths.append(3)
		else:
			x = x*6
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))