import numpy as np 

def function(x):

	o1 = 7
	s0 = x
	paths = []
	try:
		if o1 < 0:
			s0 = 4/s0
			o1 = o1-6
			x = 4-x
			paths.append(1)
		else:
			x = o1/x
			x = 1+2
			paths.append(2)
		if x <= 6:
			x = x-9
			s0 = s0+0
			o1 = 6+o1
			paths.append(3)
		else:
			x = 7-1
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))