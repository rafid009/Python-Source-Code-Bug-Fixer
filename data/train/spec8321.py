import numpy as np 

def function(x):

	a0 = 3
	s9 = 2
	paths = []
	try:
		if a0 <= 2:
			s9 = x+x
			x = s9*x
			paths.append(1)
		else:
			a0 = s9*s9
			a0 = a0+a0
			x = 3*s9
			paths.append(2)
		if x < 4:
			x = 3+x
			a0 = a0*6
			paths.append(3)
		else:
			s9 = s9-4
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))