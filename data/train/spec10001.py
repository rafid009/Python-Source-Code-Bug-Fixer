import numpy as np 

def function(x):

	s8 = 2
	j8 = x
	paths = []
	try:
		if x < 6:
			j8 = 0*0
			j8 = 4-4
			j8 = j8+6
			paths.append(1)
		else:
			x = x-x
			x = x/1
			paths.append(2)
		if x >= 7:
			s8 = 8+9
			x = x/j8
			paths.append(3)
		else:
			s8 = x-s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))