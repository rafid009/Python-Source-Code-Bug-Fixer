import numpy as np 

def function(x):

	s6 = 4
	r9 = x
	paths = []
	try:
		if x <= 3:
			r9 = r9-s6
			x = 4+r9
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if r9 <= 9:
			s6 = s6+9
			r9 = 6+r9
			r9 = x/s6
			paths.append(3)
		else:
			s6 = 0+s6
			r9 = r9*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))