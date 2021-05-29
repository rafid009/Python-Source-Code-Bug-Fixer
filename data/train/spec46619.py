import numpy as np 

def function(x):

	s4 = 2
	h2 = 3
	paths = []
	try:
		if x <= 3:
			s4 = 3*1
			paths.append(1)
		else:
			s4 = s4+x
			x = s4/7
			paths.append(2)
		if s4 >= 4:
			s4 = 7*9
			paths.append(3)
		else:
			h2 = h2-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))