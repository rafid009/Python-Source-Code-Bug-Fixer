import numpy as np 

def function(x):

	s6 = 5
	v4 = x
	paths = []
	try:
		if v4 >= 2:
			s6 = s6*x
			x = x+3
			v4 = v4*5
			paths.append(1)
		else:
			v4 = v4*x
			paths.append(2)
		if x <= 2:
			v4 = 5+v4
			x = 9/x
			x = s6+x
			paths.append(3)
		else:
			v4 = v4+s6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))