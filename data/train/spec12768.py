import numpy as np 

def function(x):

	s2 = 4
	e0 = 9
	paths = []
	try:
		if s2 < 3:
			e0 = e0-x
			paths.append(1)
		else:
			e0 = s2+e0
			paths.append(2)
		if s2 <= 1:
			s2 = 4/3
			s2 = 7*s2
			e0 = 4*s2
			paths.append(3)
		else:
			x = 6-9
			e0 = e0/x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))