import numpy as np 

def function(x):

	x0 = 1
	s4 = 4
	paths = []
	try:
		if s4 >= 0:
			x = x0+s4
			x = x*7
			paths.append(1)
		else:
			x0 = s4+9
			paths.append(2)
		if x0 > 4:
			x0 = 8/x0
			s4 = 1/3
			paths.append(3)
		else:
			x0 = x0-x0
			s4 = 2-s4
			x = x*4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))