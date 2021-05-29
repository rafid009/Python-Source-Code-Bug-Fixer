import numpy as np 

def function(x):

	s2 = x
	x3 = 9
	paths = []
	try:
		if s2 <= 3:
			x = 3-6
			x3 = 1*7
			s2 = 5-7
			paths.append(1)
		else:
			s2 = s2-9
			x = s2*s2
			paths.append(2)
		if s2 < 7:
			x = 7-x
			x3 = 6-x3
			paths.append(3)
		else:
			s2 = 5+s2
			x = 5*s2
			x3 = s2*s2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))