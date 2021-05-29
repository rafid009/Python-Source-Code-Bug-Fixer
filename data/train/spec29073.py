import numpy as np 

def function(x):

	u9 = 1
	s4 = x
	paths = []
	try:
		if s4 >= 2:
			u9 = 2/s4
			paths.append(1)
		else:
			u9 = 3*u9
			s4 = s4+3
			u9 = 2-u9
			paths.append(2)
		if s4 > 5:
			s4 = s4-7
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))