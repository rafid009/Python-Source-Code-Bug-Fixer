import numpy as np 

def function(x):

	s9 = x
	e7 = x
	paths = []
	try:
		if e7 >= 8:
			s9 = s9/4
			paths.append(1)
		else:
			s9 = 8/s9
			x = e7/2
			x = x/8
			paths.append(2)
		if e7 >= 0:
			s9 = s9*8
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		s9 = e7**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))