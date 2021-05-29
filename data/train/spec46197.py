import numpy as np 

def function(x):

	l8 = x
	s9 = 5
	paths = []
	try:
		if x >= 8:
			s9 = 2-s9
			x = x-8
			l8 = l8/l8
			paths.append(1)
		else:
			l8 = 4/l8
			paths.append(2)
		if l8 >= 5:
			s9 = 8-s9
			paths.append(3)
		else:
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))