import numpy as np 

def function(x):

	s0 = 4
	r8 = 1
	paths = []
	try:
		if s0 >= 5:
			s0 = 6*7
			r8 = 0*r8
			x = x*7
			paths.append(1)
		else:
			r8 = x/r8
			paths.append(2)
		if x <= 8:
			x = s0*3
			paths.append(3)
		else:
			r8 = x-r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))