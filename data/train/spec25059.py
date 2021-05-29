import numpy as np 

def function(x):

	o3 = 2
	s0 = x
	paths = []
	try:
		if x <= 4:
			x = x/5
			paths.append(1)
		else:
			x = 5+x
			s0 = 8+9
			s0 = s0-8
			paths.append(2)
		if x < 6:
			o3 = 9-2
			paths.append(3)
		else:
			o3 = o3+2
			x = 0-s0
			s0 = s0+6
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		o3 = s0**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))