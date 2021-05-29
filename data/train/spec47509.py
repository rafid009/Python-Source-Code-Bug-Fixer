import numpy as np 

def function(x):

	e8 = x
	s1 = x
	paths = []
	try:
		if s1 >= 6:
			s1 = s1/e8
			paths.append(1)
		else:
			s1 = s1*6
			e8 = 4+e8
			s1 = 6*s1
			paths.append(2)
		if s1 <= 2:
			s1 = s1*6
			paths.append(3)
		else:
			e8 = e8*6
			x = x-x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		e8 = s1**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))