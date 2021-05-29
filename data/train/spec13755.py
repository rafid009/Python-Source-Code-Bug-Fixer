import numpy as np 

def function(x):

	o2 = 6
	s2 = 2
	paths = []
	try:
		if s2 >= 5:
			s2 = s2+o2
			paths.append(1)
		else:
			s2 = 5/s2
			x = x*9
			o2 = 4/7
			paths.append(2)
		if x <= 4:
			o2 = o2/o2
			paths.append(3)
		else:
			o2 = 5+o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))