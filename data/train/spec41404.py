import numpy as np 

def function(x):

	s1 = 4
	j4 = x
	x = 3
	paths = []
	try:
		if s1 <= 9:
			s1 = s1+5
			paths.append(1)
		else:
			x = x-j4
			j4 = j4-x
			paths.append(2)
		if x < 1:
			x = 8/x
			s1 = 6+s1
			paths.append(3)
		else:
			x = 8-s1
			s1 = 6*5
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))