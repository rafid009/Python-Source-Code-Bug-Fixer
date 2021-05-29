import numpy as np 

def function(x):

	s1 = x
	f3 = 6
	paths = []
	try:
		if x <= 3:
			s1 = 2-s1
			x = s1/x
			paths.append(1)
		else:
			s1 = s1*8
			paths.append(2)
		if x > 9:
			x = s1+2
			f3 = 8/x
			paths.append(3)
		else:
			x = s1+x
			x = f3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))