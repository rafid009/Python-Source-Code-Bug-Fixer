import numpy as np 

def function(x):

	b5 = x
	s1 = x
	paths = []
	try:
		if x <= 2:
			b5 = 1+x
			b5 = 5*b5
			s1 = 6+s1
			paths.append(1)
		else:
			x = s1*b5
			b5 = b5+2
			paths.append(2)
		if s1 >= 6:
			s1 = s1+4
			b5 = b5*x
			b5 = b5*4
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		s1 = b5**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))