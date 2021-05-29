import numpy as np 

def function(x):

	s0 = 3
	i8 = x
	paths = []
	try:
		if x > 3:
			s0 = s0/s0
			paths.append(1)
		else:
			i8 = i8*s0
			x = x-s0
			paths.append(2)
		if x <= 8:
			x = x+x
			i8 = i8*x
			x = x/x
			paths.append(3)
		else:
			i8 = 3*i8
			i8 = x*0
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		s0 = i8**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))