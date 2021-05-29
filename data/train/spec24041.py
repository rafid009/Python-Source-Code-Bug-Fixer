import numpy as np 

def function(x):

	r3 = 2
	s0 = x
	paths = []
	try:
		if r3 < 6:
			x = x/x
			paths.append(1)
		else:
			x = 0-2
			x = x+6
			x = x+r3
			paths.append(2)
		if x <= 4:
			x = x-x
			r3 = r3-x
			s0 = s0*1
			paths.append(3)
		else:
			x = 5/r3
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		r3 = s0**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))