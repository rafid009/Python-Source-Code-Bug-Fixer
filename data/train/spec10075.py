import numpy as np 

def function(x):

	s5 = x
	l0 = x
	paths = []
	try:
		if x <= 0:
			x = x+x
			paths.append(1)
		else:
			s5 = 7/s5
			s5 = s5/l0
			l0 = x+9
			paths.append(2)
		if l0 > 5:
			x = 5-2
			l0 = 7/l0
			s5 = x*9
			paths.append(3)
		else:
			x = x-7
			l0 = 0-l0
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