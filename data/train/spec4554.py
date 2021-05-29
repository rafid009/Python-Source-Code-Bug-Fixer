import numpy as np 

def function(x):

	i8 = 2
	s0 = 5
	x = 3
	paths = []
	try:
		if s0 < 5:
			s0 = 4/s0
			s0 = s0*3
			paths.append(1)
		else:
			x = s0*9
			i8 = i8-8
			x = 7*x
			paths.append(2)
		if s0 > 6:
			i8 = 8*i8
			paths.append(3)
		else:
			s0 = 4/s0
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))