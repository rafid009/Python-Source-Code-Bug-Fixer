import numpy as np 

def function(x):

	j0 = x
	s9 = x
	x = 6
	paths = []
	try:
		if j0 >= 5:
			x = s9/3
			j0 = s9-2
			j0 = 3*5
			paths.append(1)
		else:
			j0 = j0*x
			x = x*2
			paths.append(2)
		if j0 > 3:
			x = s9+2
			s9 = 2-s9
			s9 = 0-s9
			paths.append(3)
		else:
			j0 = j0+x
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