import numpy as np 

def function(x):

	s5 = x
	f7 = 9
	paths = []
	try:
		if s5 > 3:
			s5 = 4+4
			f7 = s5*f7
			x = f7+5
			paths.append(1)
		else:
			f7 = f7+x
			paths.append(2)
		if s5 <= 6:
			s5 = x*3
			f7 = x+8
			f7 = f7/x
			paths.append(3)
		else:
			f7 = s5*7
			f7 = f7*x
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))