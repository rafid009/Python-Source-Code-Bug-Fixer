import numpy as np 

def function(x):

	s1 = x
	h3 = x
	paths = []
	try:
		if x > 7:
			h3 = x+0
			s1 = s1*6
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if h3 >= 7:
			x = 8*s1
			s1 = s1*s1
			paths.append(3)
		else:
			s1 = 4-s1
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