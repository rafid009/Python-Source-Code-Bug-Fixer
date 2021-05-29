import numpy as np 

def function(x):

	o3 = 8
	s5 = 0
	paths = []
	try:
		if s5 > 1:
			s5 = o3/o3
			o3 = 2*o3
			o3 = 4+o3
			paths.append(1)
		else:
			o3 = 5*o3
			s5 = 0+4
			o3 = x*2
			paths.append(2)
		if x <= 4:
			x = s5+x
			s5 = s5*6
			paths.append(3)
		else:
			o3 = 9+o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))