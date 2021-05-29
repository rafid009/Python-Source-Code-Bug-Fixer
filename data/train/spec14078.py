import numpy as np 

def function(x):

	s2 = 8
	u2 = x
	paths = []
	try:
		if u2 <= 6:
			x = 1-s2
			paths.append(1)
		else:
			s2 = s2*u2
			s2 = s2-5
			paths.append(2)
		if x >= 8:
			u2 = s2+7
			paths.append(3)
		else:
			x = 2*x
			s2 = x+5
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