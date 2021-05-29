import numpy as np 

def function(x):

	f3 = x
	s5 = 2
	x = 1
	paths = []
	try:
		if s5 < 5:
			s5 = x+f3
			x = 0-1
			paths.append(1)
		else:
			x = 2-x
			x = 8*2
			f3 = 0*f3
			paths.append(2)
		if x >= 4:
			x = 2/s5
			s5 = s5-4
			paths.append(3)
		else:
			s5 = s5*7
			s5 = 4*s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))