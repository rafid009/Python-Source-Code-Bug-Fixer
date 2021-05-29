import numpy as np 

def function(x):

	s0 = 2
	f9 = x
	paths = []
	try:
		if f9 >= 3:
			f9 = f9+8
			f9 = 0-f9
			paths.append(1)
		else:
			s0 = 9+f9
			paths.append(2)
		if s0 > 8:
			f9 = 7-9
			paths.append(3)
		else:
			f9 = s0*f9
			s0 = 6+f9
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		f9 = s0**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))