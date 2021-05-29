import numpy as np 

def function(x):

	j4 = 7
	s1 = 5
	paths = []
	try:
		if x < 4:
			j4 = j4*9
			s1 = 1-s1
			x = j4*s1
			paths.append(1)
		else:
			s1 = 8-s1
			s1 = x+s1
			paths.append(2)
		if s1 <= 8:
			s1 = 1*s1
			x = x-7
			paths.append(3)
		else:
			s1 = s1-j4
			x = j4+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))