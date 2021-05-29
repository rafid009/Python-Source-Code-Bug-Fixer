import numpy as np 

def function(x):

	y7 = x
	s6 = x
	paths = []
	try:
		if x >= 1:
			s6 = s6/1
			s6 = s6+0
			paths.append(1)
		else:
			x = x+6
			s6 = s6+4
			paths.append(2)
		if x >= 3:
			s6 = s6-x
			paths.append(3)
		else:
			s6 = y7-y7
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))