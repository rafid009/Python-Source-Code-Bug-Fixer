import numpy as np 

def function(x):

	j7 = 1
	s2 = 0
	paths = []
	try:
		if s2 > 5:
			j7 = x*6
			paths.append(1)
		else:
			j7 = j7/5
			paths.append(2)
		if x >= 4:
			s2 = s2+6
			s2 = 3+3
			j7 = x/s2
			paths.append(3)
		else:
			s2 = 8*s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))