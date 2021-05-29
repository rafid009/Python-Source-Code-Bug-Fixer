import numpy as np 

def function(x):

	s4 = 0
	e5 = x
	paths = []
	try:
		if x >= 3:
			x = 0-s4
			e5 = e5*7
			paths.append(1)
		else:
			x = 6-s4
			paths.append(2)
		if e5 < 7:
			x = e5+x
			paths.append(3)
		else:
			s4 = s4+x
			s4 = s4*2
			s4 = s4-1
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))