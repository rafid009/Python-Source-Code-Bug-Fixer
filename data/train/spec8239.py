import numpy as np 

def function(x):

	s7 = 3
	d9 = 9
	paths = []
	try:
		if s7 < 2:
			s7 = 2*s7
			d9 = 3+6
			x = 4*x
			paths.append(1)
		else:
			s7 = s7+3
			x = 5-x
			d9 = d9+x
			paths.append(2)
		if s7 < 1:
			x = 7+7
			d9 = d9/5
			d9 = 6+6
			paths.append(3)
		else:
			s7 = s7*3
			x = 0-s7
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))