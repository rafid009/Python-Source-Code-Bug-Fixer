import numpy as np 

def function(x):

	k6 = x
	s2 = x
	x = x
	paths = []
	try:
		if k6 >= 8:
			x = x*7
			s2 = 3+0
			s2 = s2-9
			paths.append(1)
		else:
			k6 = x-k6
			x = 2/x
			s2 = 8-5
			paths.append(2)
		if s2 >= 4:
			k6 = k6+9
			x = 1+6
			x = 4*x
			paths.append(3)
		else:
			x = 5-k6
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))