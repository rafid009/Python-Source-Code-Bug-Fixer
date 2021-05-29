import numpy as np 

def function(x):

	x2 = 1
	s2 = 9
	paths = []
	try:
		if s2 < 4:
			x2 = s2+7
			s2 = s2/3
			x2 = s2-x2
			paths.append(1)
		else:
			x2 = x2/6
			s2 = s2+x
			x2 = x2-x
			paths.append(2)
		if s2 > 9:
			s2 = x2*s2
			s2 = 5-2
			paths.append(3)
		else:
			s2 = 4-s2
			x2 = 3*x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))