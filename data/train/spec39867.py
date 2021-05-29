import numpy as np 

def function(x):

	s6 = x
	y6 = 4
	paths = []
	try:
		if y6 < 1:
			s6 = y6/s6
			paths.append(1)
		else:
			y6 = x-9
			paths.append(2)
		if s6 <= 4:
			y6 = 9-y6
			s6 = s6+9
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		y6 = s6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))