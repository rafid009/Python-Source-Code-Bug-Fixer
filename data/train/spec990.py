import numpy as np 

def function(x):

	s4 = 5
	j6 = x
	paths = []
	try:
		if s4 > 9:
			x = s4-4
			j6 = s4-s4
			paths.append(1)
		else:
			s4 = 6-s4
			s4 = s4-1
			s4 = s4*4
			paths.append(2)
		if s4 > 0:
			x = x+s4
			s4 = 3-8
			s4 = 1-s4
			paths.append(3)
		else:
			j6 = j6+s4
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