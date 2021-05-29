import numpy as np 

def function(x):

	v0 = 4
	s8 = x
	paths = []
	try:
		if x < 1:
			s8 = 4*s8
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x < 7:
			s8 = 4/s8
			paths.append(3)
		else:
			x = v0+4
			x = x-x
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))