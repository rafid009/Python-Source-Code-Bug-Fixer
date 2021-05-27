import numpy as np 

def function(x):

	s6 = 9
	e0 = 3
	paths = []
	try:
		if e0 > 2:
			s6 = s6-x
			e0 = s6-4
			paths.append(1)
		else:
			s6 = 3+7
			e0 = e0-e0
			s6 = 0*s6
			paths.append(2)
		if e0 < 0:
			x = 9/1
			x = 2*0
			paths.append(3)
		else:
			x = 3-s6
			s6 = x+e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		s6 = e0**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))