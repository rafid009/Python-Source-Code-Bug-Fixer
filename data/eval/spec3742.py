import numpy as np 

def function(x):

	s0 = x
	r6 = x
	paths = []
	try:
		if x <= 7:
			r6 = r6-x
			paths.append(1)
		else:
			r6 = x/r6
			x = x*x
			paths.append(2)
		if r6 >= 9:
			x = 8*r6
			r6 = r6*9
			paths.append(3)
		else:
			s0 = 4-s0
			s0 = s0-x
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