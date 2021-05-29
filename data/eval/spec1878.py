import numpy as np 

def function(x):

	s6 = x
	e6 = 9
	paths = []
	try:
		if e6 <= 0:
			e6 = e6-7
			paths.append(1)
		else:
			s6 = 8+x
			paths.append(2)
		if s6 >= 9:
			e6 = s6+x
			paths.append(3)
		else:
			e6 = 0*7
			e6 = e6-9
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))