import numpy as np 

def function(x):

	j3 = x
	s9 = x
	paths = []
	try:
		if j3 >= 8:
			j3 = 4+6
			paths.append(1)
		else:
			s9 = s9-x
			paths.append(2)
		if s9 < 8:
			x = x+8
			s9 = s9-8
			j3 = 9+j3
			paths.append(3)
		else:
			s9 = 2*3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		s9 = j3**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))