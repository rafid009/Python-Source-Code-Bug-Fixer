import numpy as np 

def function(x):

	v5 = x
	s8 = 2
	paths = []
	try:
		if v5 > 1:
			x = 7*9
			s8 = s8+x
			s8 = 0*s8
			paths.append(1)
		else:
			v5 = 6*v5
			v5 = v5/3
			x = 9*x
			paths.append(2)
		if s8 < 1:
			s8 = 9*s8
			v5 = x-4
			x = x+3
			paths.append(3)
		else:
			v5 = v5/6
			s8 = s8-v5
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		s8 = v5**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))