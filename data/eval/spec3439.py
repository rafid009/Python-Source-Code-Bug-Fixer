import numpy as np 

def function(x):

	s7 = x
	j4 = 2
	paths = []
	try:
		if j4 > 4:
			x = 8+1
			s7 = 7-9
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x > 2:
			j4 = x-9
			x = 9*x
			j4 = j4*x
			paths.append(3)
		else:
			x = 2+x
			s7 = s7/x
			s7 = 6-s7
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