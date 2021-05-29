import numpy as np 

def function(x):

	s5 = 3
	y3 = 1
	paths = []
	try:
		if x > 9:
			y3 = y3-5
			paths.append(1)
		else:
			y3 = y3-0
			s5 = 4*s5
			s5 = s5-1
			paths.append(2)
		if x > 3:
			s5 = x*9
			x = s5-0
			paths.append(3)
		else:
			x = x*s5
			s5 = 8/s5
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		s5 = y3**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))