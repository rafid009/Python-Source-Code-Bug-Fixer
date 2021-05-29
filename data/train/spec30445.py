import numpy as np 

def function(x):

	h7 = 3
	s6 = x
	paths = []
	try:
		if x <= 2:
			h7 = 8*h7
			x = x*1
			paths.append(1)
		else:
			x = x+x
			x = 1-x
			h7 = 2/x
			paths.append(2)
		if h7 <= 0:
			h7 = h7+s6
			x = 4+1
			x = x/7
			paths.append(3)
		else:
			s6 = s6+1
			h7 = 9-h7
			h7 = h7*6
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