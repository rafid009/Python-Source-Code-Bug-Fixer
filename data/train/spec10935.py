import numpy as np 

def function(x):

	s6 = 6
	h4 = 9
	paths = []
	try:
		if h4 > 0:
			h4 = x-x
			s6 = 8+s6
			x = x*0
			paths.append(1)
		else:
			x = x*8
			s6 = s6-x
			paths.append(2)
		if s6 <= 8:
			x = x-8
			paths.append(3)
		else:
			s6 = s6/1
			h4 = 3-9
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		s6 = h4**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))