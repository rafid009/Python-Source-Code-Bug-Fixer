import numpy as np 

def function(x):

	s6 = x
	e9 = 6
	paths = []
	try:
		if x >= 4:
			s6 = 8+x
			e9 = 4*x
			paths.append(1)
		else:
			e9 = e9+s6
			x = x+e9
			x = 7-0
			paths.append(2)
		if x >= 5:
			x = x-4
			s6 = 5-s6
			e9 = e9+e9
			paths.append(3)
		else:
			e9 = s6-1
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		s6 = e9**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))