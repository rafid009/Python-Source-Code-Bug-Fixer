import numpy as np 

def function(x):

	v2 = x
	s0 = 5
	x = x
	paths = []
	try:
		if x <= 3:
			x = x/5
			v2 = v2-7
			x = x-7
			paths.append(1)
		else:
			s0 = s0-8
			v2 = s0+v2
			v2 = 9/5
			paths.append(2)
		if v2 > 6:
			s0 = v2+4
			paths.append(3)
		else:
			x = 9/x
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