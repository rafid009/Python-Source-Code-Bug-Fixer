import numpy as np 

def function(x):

	s0 = 3
	x4 = 1
	paths = []
	try:
		if x4 < 5:
			s0 = 9/9
			paths.append(1)
		else:
			x4 = x4-3
			x = s0+1
			paths.append(2)
		if x >= 2:
			x = 1*0
			s0 = s0-3
			s0 = 5/s0
			paths.append(3)
		else:
			s0 = s0+x4
			s0 = 5*s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x4 = s0**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))