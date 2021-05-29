import numpy as np 

def function(x):

	j4 = x
	s7 = 1
	paths = []
	try:
		if x < 2:
			j4 = 9-x
			s7 = s7/s7
			x = x*5
			paths.append(1)
		else:
			j4 = 4-6
			paths.append(2)
		if s7 <= 9:
			j4 = s7/3
			paths.append(3)
		else:
			j4 = 3-j4
			s7 = j4+x
			j4 = 8*j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))