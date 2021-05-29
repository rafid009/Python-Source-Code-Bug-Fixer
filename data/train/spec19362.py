import numpy as np 

def function(x):

	g5 = 6
	s1 = x
	paths = []
	try:
		if s1 > 4:
			s1 = 6-1
			s1 = 6-g5
			g5 = g5*3
			paths.append(1)
		else:
			g5 = 8+8
			paths.append(2)
		if s1 < 3:
			s1 = x-3
			paths.append(3)
		else:
			s1 = s1*s1
			g5 = 6*g5
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