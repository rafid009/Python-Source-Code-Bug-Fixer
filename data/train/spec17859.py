import numpy as np 

def function(x):

	l5 = 6
	s1 = 0
	paths = []
	try:
		if l5 >= 9:
			l5 = 7/l5
			x = 1-0
			l5 = l5-l5
			paths.append(1)
		else:
			s1 = s1*6
			paths.append(2)
		if x < 3:
			x = 9*x
			s1 = 4+s1
			x = 9*x
			paths.append(3)
		else:
			s1 = 4+0
			l5 = x*7
			s1 = 5+s1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))