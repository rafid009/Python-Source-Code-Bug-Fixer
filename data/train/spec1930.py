import numpy as np 

def function(x):

	y8 = x
	s9 = 8
	paths = []
	try:
		if x < 0:
			y8 = y8+x
			y8 = y8*x
			paths.append(1)
		else:
			x = 7+x
			x = s9/5
			x = 4*7
			paths.append(2)
		if x > 8:
			s9 = s9*3
			s9 = s9+x
			paths.append(3)
		else:
			x = s9-7
			s9 = 2-s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		y8 = s9**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))