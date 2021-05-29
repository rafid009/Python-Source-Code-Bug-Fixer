import numpy as np 

def function(x):

	v9 = x
	s2 = 2
	x = 5
	paths = []
	try:
		if x < 9:
			s2 = s2/v9
			paths.append(1)
		else:
			s2 = 7-x
			paths.append(2)
		if v9 >= 3:
			v9 = 1/8
			v9 = v9-8
			paths.append(3)
		else:
			x = 0/x
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