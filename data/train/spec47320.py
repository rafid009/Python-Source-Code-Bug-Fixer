import numpy as np 

def function(x):

	s1 = 3
	a3 = x
	paths = []
	try:
		if s1 >= 9:
			s1 = s1-5
			a3 = x+x
			a3 = a3*s1
			paths.append(1)
		else:
			s1 = 3+s1
			a3 = 5*a3
			paths.append(2)
		if a3 > 4:
			x = x+8
			a3 = 1/a3
			paths.append(3)
		else:
			a3 = 2-a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		s1 = a3**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))