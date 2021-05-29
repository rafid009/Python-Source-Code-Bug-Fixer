import numpy as np 

def function(x):

	s0 = x
	y5 = 6
	paths = []
	try:
		if s0 >= 3:
			y5 = x/y5
			s0 = s0-s0
			y5 = 6+y5
			paths.append(1)
		else:
			x = 9+x
			y5 = y5-0
			y5 = 5/1
			paths.append(2)
		if s0 < 4:
			x = x+6
			s0 = 2*s0
			paths.append(3)
		else:
			s0 = s0+6
			y5 = x*5
			x = x*0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))