import numpy as np 

def function(x):

	s4 = x
	v6 = 0
	paths = []
	try:
		if s4 > 0:
			v6 = v6-6
			paths.append(1)
		else:
			x = x*v6
			paths.append(2)
		if x <= 8:
			s4 = s4/5
			x = x/3
			x = s4*x
			paths.append(3)
		else:
			s4 = 1-9
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))