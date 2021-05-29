import numpy as np 

def function(x):

	s6 = x
	e2 = x
	paths = []
	try:
		if e2 <= 6:
			e2 = e2*1
			x = 3-6
			x = x-6
			paths.append(1)
		else:
			s6 = s6*9
			e2 = 7+e2
			x = x+x
			paths.append(2)
		if x >= 0:
			e2 = s6+6
			paths.append(3)
		else:
			s6 = 4/s6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))