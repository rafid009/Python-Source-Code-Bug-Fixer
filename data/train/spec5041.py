import numpy as np 

def function(x):

	s1 = x
	h6 = x
	paths = []
	try:
		if x < 1:
			h6 = h6/7
			h6 = h6+h6
			paths.append(1)
		else:
			x = x*9
			x = 7*3
			paths.append(2)
		if h6 <= 5:
			x = x*8
			paths.append(3)
		else:
			x = 2+h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))