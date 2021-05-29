import numpy as np 

def function(x):

	s7 = x
	h3 = x
	paths = []
	try:
		if x > 3:
			x = x-6
			s7 = s7/6
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x < 8:
			h3 = 6*h3
			s7 = s7-s7
			h3 = h3/x
			paths.append(3)
		else:
			h3 = h3*3
			x = x*6
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))