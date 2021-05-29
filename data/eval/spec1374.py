import numpy as np 

def function(x):

	t0 = x
	s5 = 6
	paths = []
	try:
		if x < 2:
			s5 = s5-t0
			x = x-2
			paths.append(1)
		else:
			s5 = 4+s5
			paths.append(2)
		if s5 >= 9:
			x = t0+x
			paths.append(3)
		else:
			x = x+7
			s5 = s5*5
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		s5 = t0**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))