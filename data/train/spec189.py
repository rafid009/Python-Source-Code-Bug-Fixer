import numpy as np 

def function(x):

	s9 = 5
	y2 = 5
	paths = []
	try:
		if s9 < 3:
			x = 1/9
			s9 = s9+s9
			paths.append(1)
		else:
			s9 = 8*3
			s9 = 9+x
			x = 8+8
			paths.append(2)
		if s9 < 7:
			x = 6/9
			paths.append(3)
		else:
			x = 8+x
			x = 5*6
			x = 0-6
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