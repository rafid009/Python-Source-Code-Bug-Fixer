import numpy as np 

def function(x):

	x9 = 7
	s6 = 0
	paths = []
	try:
		if s6 >= 6:
			x = x-5
			s6 = x9-8
			x = 9-7
			paths.append(1)
		else:
			s6 = 8*9
			paths.append(2)
		if x9 <= 5:
			s6 = s6*5
			paths.append(3)
		else:
			s6 = x/s6
			x9 = 8*x9
			x9 = 6+9
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