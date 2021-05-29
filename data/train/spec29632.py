import numpy as np 

def function(x):

	s0 = x
	f5 = x
	paths = []
	try:
		if f5 > 1:
			f5 = 2-f5
			paths.append(1)
		else:
			s0 = s0*s0
			s0 = f5+s0
			f5 = f5/1
			paths.append(2)
		if x >= 1:
			f5 = 0-f5
			paths.append(3)
		else:
			s0 = 9-s0
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))