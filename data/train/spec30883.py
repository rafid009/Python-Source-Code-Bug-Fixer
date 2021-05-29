import numpy as np 

def function(x):

	j4 = 1
	s1 = x
	paths = []
	try:
		if s1 < 3:
			s1 = 8/s1
			paths.append(1)
		else:
			x = x-x
			j4 = j4/4
			paths.append(2)
		if x < 5:
			j4 = 5*j4
			j4 = j4*5
			paths.append(3)
		else:
			j4 = j4-j4
			j4 = 0-4
			j4 = 9+j4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))