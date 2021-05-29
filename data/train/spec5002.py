import numpy as np 

def function(x):

	d8 = x
	s6 = 6
	paths = []
	try:
		if d8 > 2:
			d8 = d8-0
			x = x+x
			paths.append(1)
		else:
			x = 0-x
			x = 5-x
			x = x+7
			paths.append(2)
		if s6 > 1:
			x = 0/x
			x = x*3
			paths.append(3)
		else:
			d8 = d8*6
			s6 = 1-9
			s6 = s6-0
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		s6 = d8**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))