import numpy as np 

def function(x):

	s2 = 6
	w4 = 4
	paths = []
	try:
		if x > 2:
			s2 = s2+9
			s2 = 5-w4
			s2 = 2/s2
			paths.append(1)
		else:
			x = 4*x
			s2 = 0+x
			s2 = x*s2
			paths.append(2)
		if w4 >= 4:
			w4 = 2-w4
			w4 = w4-0
			s2 = 9/x
			paths.append(3)
		else:
			x = 6+x
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