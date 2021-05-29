import numpy as np 

def function(x):

	a8 = 4
	s5 = x
	paths = []
	try:
		if s5 >= 8:
			x = x/6
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if a8 > 3:
			s5 = 2+s5
			x = 5-x
			x = x*a8
			paths.append(3)
		else:
			a8 = a8+0
			a8 = 5+a8
			x = x*8
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