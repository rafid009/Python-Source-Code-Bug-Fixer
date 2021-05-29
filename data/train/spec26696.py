import numpy as np 

def function(x):

	j6 = x
	s7 = 1
	paths = []
	try:
		if s7 < 9:
			x = 9+x
			paths.append(1)
		else:
			x = s7+x
			j6 = 2*j6
			paths.append(2)
		if x > 9:
			s7 = 3*s7
			j6 = j6+j6
			paths.append(3)
		else:
			s7 = 6-s7
			x = j6+x
			s7 = 6-9
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		j6 = s7**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))