import numpy as np 

def function(x):

	a4 = x
	s0 = x
	paths = []
	try:
		if s0 >= 4:
			a4 = 2+a4
			s0 = s0*9
			a4 = 6-4
			paths.append(1)
		else:
			a4 = 3*a4
			x = x+s0
			x = x+7
			paths.append(2)
		if x >= 6:
			s0 = s0*9
			a4 = 6/8
			x = s0+8
			paths.append(3)
		else:
			x = s0-a4
			x = 8*x
			s0 = 8/s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		a4 = s0**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))