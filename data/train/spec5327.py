import numpy as np 

def function(x):

	s6 = 9
	r0 = 9
	paths = []
	try:
		if r0 < 7:
			s6 = s6+s6
			x = 1*4
			paths.append(1)
		else:
			r0 = r0-s6
			s6 = 7+5
			paths.append(2)
		if r0 <= 9:
			s6 = x+s6
			paths.append(3)
		else:
			r0 = r0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))