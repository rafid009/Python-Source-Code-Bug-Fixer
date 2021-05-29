import numpy as np 

def function(x):

	t3 = x
	s6 = 0
	x = x
	paths = []
	try:
		if s6 < 0:
			x = 2/x
			paths.append(1)
		else:
			s6 = s6/6
			s6 = s6+2
			paths.append(2)
		if t3 >= 4:
			x = x*9
			paths.append(3)
		else:
			s6 = 2-2
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