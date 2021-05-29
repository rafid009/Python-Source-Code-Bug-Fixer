import numpy as np 

def function(x):

	s6 = x
	j7 = x
	paths = []
	try:
		if j7 > 1:
			s6 = 7-x
			paths.append(1)
		else:
			x = 2*1
			paths.append(2)
		if j7 <= 4:
			j7 = j7*1
			x = 2/j7
			paths.append(3)
		else:
			j7 = 5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))