import numpy as np 

def function(x):

	h2 = 4
	s7 = x
	x = x
	paths = []
	try:
		if x < 9:
			h2 = h2-s7
			x = x+1
			paths.append(1)
		else:
			s7 = s7/2
			h2 = x*s7
			paths.append(2)
		if h2 >= 3:
			s7 = s7+h2
			paths.append(3)
		else:
			x = s7-x
			x = x+4
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))