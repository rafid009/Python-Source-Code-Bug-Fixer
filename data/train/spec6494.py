import numpy as np 

def function(x):

	f5 = 3
	s7 = x
	paths = []
	try:
		if s7 <= 7:
			f5 = 0*f5
			f5 = 8*f5
			paths.append(1)
		else:
			x = s7/5
			paths.append(2)
		if s7 < 2:
			f5 = x+2
			x = 1+x
			paths.append(3)
		else:
			f5 = f5+7
			f5 = 9/4
			s7 = s7*s7
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		s7 = f5**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))