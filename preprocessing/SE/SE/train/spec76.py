import numpy as np 

def function(x):

	h2 = 0
	s7 = x
	paths = []
	try:
		if x < 9:
			s7 = s7/6
			paths.append(1)
		else:
			x = x+x
			h2 = 6-h2
			x = 2+s7
			paths.append(2)
		if s7 >= 6:
			h2 = h2-x
			s7 = s7/s7
			s7 = s7/1
			paths.append(3)
		else:
			h2 = h2-5
			s7 = s7*5
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		s7 = h2**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))