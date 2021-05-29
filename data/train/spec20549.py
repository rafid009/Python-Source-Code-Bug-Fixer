import numpy as np 

def function(x):

	d8 = 1
	s4 = 8
	paths = []
	try:
		if s4 <= 1:
			s4 = 1-s4
			paths.append(1)
		else:
			d8 = d8*7
			paths.append(2)
		if d8 < 7:
			x = 2-6
			paths.append(3)
		else:
			s4 = s4*1
			s4 = s4*s4
			x = x+6
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