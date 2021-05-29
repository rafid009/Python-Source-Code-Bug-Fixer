import numpy as np 

def function(x):

	o3 = 3
	s4 = x
	paths = []
	try:
		if s4 > 0:
			o3 = x/s4
			paths.append(1)
		else:
			o3 = o3*9
			paths.append(2)
		if s4 < 1:
			s4 = 8/s4
			s4 = s4+3
			s4 = o3-x
			paths.append(3)
		else:
			o3 = o3/o3
			s4 = o3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))