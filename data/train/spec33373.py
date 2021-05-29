import numpy as np 

def function(x):

	h6 = 7
	s1 = x
	paths = []
	try:
		if x >= 1:
			s1 = s1*5
			x = x-9
			x = x+9
			paths.append(1)
		else:
			s1 = s1*1
			h6 = x/h6
			x = x-3
			paths.append(2)
		if s1 < 9:
			s1 = 0/s1
			s1 = x+h6
			paths.append(3)
		else:
			s1 = h6+x
			x = s1-9
			s1 = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))