import numpy as np 

def function(x):

	s1 = x
	e5 = x
	paths = []
	try:
		if s1 < 5:
			x = x-x
			e5 = e5/6
			x = x+s1
			paths.append(1)
		else:
			x = 8/x
			e5 = e5+e5
			s1 = 8/e5
			paths.append(2)
		if x > 0:
			e5 = e5/s1
			s1 = s1-e5
			x = e5*3
			paths.append(3)
		else:
			s1 = s1+7
			s1 = 2*s1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))