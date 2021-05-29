import numpy as np 

def function(x):

	h3 = x
	s1 = 4
	paths = []
	try:
		if x < 6:
			h3 = 5/h3
			s1 = s1/8
			paths.append(1)
		else:
			h3 = h3*1
			s1 = s1-9
			h3 = h3*h3
			paths.append(2)
		if h3 < 7:
			h3 = 6*6
			paths.append(3)
		else:
			x = x/6
			x = 6/h3
			x = s1/7
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