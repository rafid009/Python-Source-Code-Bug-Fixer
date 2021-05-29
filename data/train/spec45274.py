import numpy as np 

def function(x):

	s8 = x
	o3 = x
	paths = []
	try:
		if o3 <= 3:
			x = x+x
			o3 = 4+o3
			paths.append(1)
		else:
			s8 = s8*x
			o3 = s8*1
			paths.append(2)
		if x < 1:
			x = s8+x
			paths.append(3)
		else:
			s8 = s8-1
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		s8 = o3**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))