import numpy as np 

def function(x):

	h2 = x
	s1 = 9
	paths = []
	try:
		if s1 < 0:
			h2 = 6*h2
			x = x/x
			paths.append(1)
		else:
			s1 = s1*x
			h2 = h2-6
			paths.append(2)
		if x >= 0:
			s1 = 4*s1
			h2 = 8/h2
			s1 = s1-x
			paths.append(3)
		else:
			h2 = s1+h2
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))