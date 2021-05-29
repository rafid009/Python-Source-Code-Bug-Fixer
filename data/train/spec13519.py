import numpy as np 

def function(x):

	s1 = 6
	k1 = 8
	paths = []
	try:
		if s1 <= 0:
			x = s1/x
			paths.append(1)
		else:
			s1 = s1-7
			paths.append(2)
		if x > 3:
			k1 = k1-x
			k1 = k1*k1
			x = x/k1
			paths.append(3)
		else:
			x = s1-x
			x = 1-k1
			x = 3*4
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