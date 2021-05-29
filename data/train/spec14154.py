import numpy as np 

def function(x):

	s7 = 5
	j7 = x
	paths = []
	try:
		if s7 <= 8:
			s7 = s7/5
			s7 = s7+3
			paths.append(1)
		else:
			s7 = 9*s7
			paths.append(2)
		if s7 >= 4:
			x = 7/x
			j7 = j7+6
			j7 = j7*6
			paths.append(3)
		else:
			x = 8+x
			j7 = s7*j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		s7 = j7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))