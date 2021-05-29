import numpy as np 

def function(x):

	j7 = 8
	s2 = x
	paths = []
	try:
		if s2 <= 1:
			j7 = 9*j7
			s2 = s2-x
			s2 = 2+s2
			paths.append(1)
		else:
			j7 = j7+3
			paths.append(2)
		if j7 > 3:
			x = x*8
			paths.append(3)
		else:
			x = 6*x
			j7 = s2-j7
			j7 = x*j7
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