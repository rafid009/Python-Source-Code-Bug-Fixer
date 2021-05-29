import numpy as np 

def function(x):

	s0 = 8
	r5 = x
	paths = []
	try:
		if x < 8:
			x = 9-x
			r5 = r5/1
			r5 = 9*3
			paths.append(1)
		else:
			x = x*9
			r5 = 9*x
			paths.append(2)
		if r5 < 1:
			x = x*8
			x = r5+6
			paths.append(3)
		else:
			s0 = 4-s0
			s0 = s0-2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		r5 = s0**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))