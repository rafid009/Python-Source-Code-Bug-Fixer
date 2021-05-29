import numpy as np 

def function(x):

	h4 = x
	s4 = 9
	paths = []
	try:
		if h4 <= 0:
			s4 = h4/3
			h4 = h4+7
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if s4 > 3:
			s4 = 8+s4
			s4 = 7*9
			s4 = x*s4
			paths.append(3)
		else:
			h4 = h4*x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		h4 = s4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))