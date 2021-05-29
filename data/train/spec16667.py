import numpy as np 

def function(x):

	s1 = 9
	l5 = 8
	paths = []
	try:
		if l5 >= 4:
			s1 = 7-s1
			x = x/9
			x = x+7
			paths.append(1)
		else:
			s1 = s1-6
			x = 3+x
			s1 = 9*8
			paths.append(2)
		if l5 < 4:
			l5 = 2+s1
			s1 = s1-2
			l5 = 2+4
			paths.append(3)
		else:
			l5 = l5*s1
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		s1 = l5**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))