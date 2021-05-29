import numpy as np 

def function(x):

	s2 = x
	l0 = x
	paths = []
	try:
		if s2 <= 3:
			l0 = s2*0
			paths.append(1)
		else:
			l0 = 2/x
			paths.append(2)
		if s2 >= 2:
			s2 = s2-6
			l0 = 6-3
			paths.append(3)
		else:
			s2 = l0-3
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