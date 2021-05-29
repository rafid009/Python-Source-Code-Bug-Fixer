import numpy as np 

def function(x):

	i8 = 4
	s0 = 0
	paths = []
	try:
		if s0 >= 5:
			x = 5+x
			paths.append(1)
		else:
			s0 = s0/8
			s0 = 0+8
			x = x*i8
			paths.append(2)
		if i8 > 9:
			s0 = s0-2
			paths.append(3)
		else:
			x = x-0
			s0 = 8+x
			x = x/3
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		i8 = s0**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))