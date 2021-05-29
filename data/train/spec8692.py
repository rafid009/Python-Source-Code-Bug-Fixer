import numpy as np 

def function(x):

	d8 = 3
	s2 = x
	paths = []
	try:
		if x >= 1:
			s2 = d8+5
			x = s2*x
			paths.append(1)
		else:
			x = d8+3
			x = d8*4
			paths.append(2)
		if x <= 9:
			s2 = 1/s2
			paths.append(3)
		else:
			s2 = 4+s2
			d8 = 0-3
			x = 7*2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))