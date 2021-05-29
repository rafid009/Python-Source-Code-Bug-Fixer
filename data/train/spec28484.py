import numpy as np 

def function(x):

	s0 = 2
	f2 = x
	paths = []
	try:
		if x > 2:
			x = x+4
			f2 = f2/3
			paths.append(1)
		else:
			s0 = x+9
			paths.append(2)
		if f2 > 9:
			x = 9-9
			paths.append(3)
		else:
			f2 = 6-s0
			s0 = s0+7
			x = x+5
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		s0 = f2**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))