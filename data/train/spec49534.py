import numpy as np 

def function(x):

	s1 = 1
	v1 = 6
	paths = []
	try:
		if s1 < 3:
			x = 6/x
			s1 = 6/s1
			paths.append(1)
		else:
			v1 = v1*4
			x = x+x
			paths.append(2)
		if x >= 9:
			x = 7*v1
			x = x-0
			v1 = 1*v1
			paths.append(3)
		else:
			x = x-4
			s1 = 4-s1
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