import numpy as np 

def function(x):

	v9 = x
	s7 = 5
	paths = []
	try:
		if v9 > 5:
			x = x-3
			v9 = s7*8
			paths.append(1)
		else:
			x = x-x
			v9 = v9+0
			x = 2+x
			paths.append(2)
		if s7 <= 6:
			s7 = s7/x
			x = v9*2
			x = x/8
			paths.append(3)
		else:
			s7 = 9/s7
			v9 = s7+v9
			s7 = s7*v9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))