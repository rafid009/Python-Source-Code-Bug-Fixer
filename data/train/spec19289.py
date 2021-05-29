import numpy as np 

def function(x):

	m3 = 8
	s4 = 0
	paths = []
	try:
		if x <= 2:
			x = 4+x
			s4 = x*1
			paths.append(1)
		else:
			x = 7-2
			s4 = 7-s4
			paths.append(2)
		if s4 < 7:
			x = 5*x
			x = x-8
			s4 = 4-s4
			paths.append(3)
		else:
			m3 = 8-4
			s4 = 8*8
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