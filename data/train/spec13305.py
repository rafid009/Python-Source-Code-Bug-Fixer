import numpy as np 

def function(x):

	o3 = x
	s7 = x
	paths = []
	try:
		if x > 1:
			x = s7-x
			s7 = s7-9
			o3 = 2-o3
			paths.append(1)
		else:
			o3 = 2-s7
			o3 = 6/o3
			paths.append(2)
		if o3 <= 8:
			o3 = 6/o3
			s7 = s7/7
			s7 = s7/5
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))