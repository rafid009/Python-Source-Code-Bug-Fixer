import numpy as np 

def function(x):

	a0 = x
	s1 = 0
	paths = []
	try:
		if x < 0:
			x = 3*x
			paths.append(1)
		else:
			s1 = 3+7
			paths.append(2)
		if x > 7:
			s1 = s1/5
			s1 = 7-a0
			a0 = 6+a0
			paths.append(3)
		else:
			a0 = a0-a0
			x = 7-x
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