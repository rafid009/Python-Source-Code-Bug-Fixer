import numpy as np 

def function(x):

	h3 = 8
	s4 = 8
	paths = []
	try:
		if x < 8:
			h3 = x/h3
			s4 = s4-6
			paths.append(1)
		else:
			s4 = 0+h3
			s4 = 4-s4
			paths.append(2)
		if x > 0:
			x = 0/h3
			s4 = 4*s4
			paths.append(3)
		else:
			x = 5*x
			h3 = h3/6
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))