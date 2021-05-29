import numpy as np 

def function(x):

	h1 = x
	s9 = 7
	paths = []
	try:
		if s9 > 3:
			x = 2+3
			s9 = s9/3
			paths.append(1)
		else:
			h1 = 4/h1
			s9 = s9-9
			s9 = h1+x
			paths.append(2)
		if h1 < 7:
			h1 = h1-5
			s9 = 0-6
			paths.append(3)
		else:
			h1 = h1-x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		h1 = s9**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))