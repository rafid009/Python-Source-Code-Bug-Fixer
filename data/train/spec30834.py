import numpy as np 

def function(x):

	s2 = 9
	l6 = x
	paths = []
	try:
		if x >= 9:
			x = 7-9
			x = s2/5
			paths.append(1)
		else:
			s2 = s2/6
			s2 = 4/9
			x = x+x
			paths.append(2)
		if s2 < 1:
			x = x+9
			l6 = 5+7
			s2 = s2*3
			paths.append(3)
		else:
			x = 8+x
			s2 = x*1
			s2 = x*s2
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