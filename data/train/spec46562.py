import numpy as np 

def function(x):

	s4 = x
	i0 = 8
	paths = []
	try:
		if s4 < 1:
			i0 = 9*i0
			s4 = s4-9
			s4 = s4/s4
			paths.append(1)
		else:
			i0 = s4/5
			s4 = i0-s4
			paths.append(2)
		if x > 1:
			x = i0*i0
			paths.append(3)
		else:
			s4 = x*s4
			i0 = 3-i0
			x = x*5
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))