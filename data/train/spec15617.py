import numpy as np 

def function(x):

	q0 = x
	s9 = 6
	paths = []
	try:
		if s9 >= 3:
			x = q0+x
			paths.append(1)
		else:
			x = 5+2
			x = x/q0
			paths.append(2)
		if q0 >= 8:
			q0 = 7+q0
			x = x*7
			x = x-2
			paths.append(3)
		else:
			s9 = 7-s9
			q0 = 0+q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		s9 = q0**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))