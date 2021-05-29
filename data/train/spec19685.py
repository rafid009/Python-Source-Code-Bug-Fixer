import numpy as np 

def function(x):

	s1 = 7
	b8 = 7
	paths = []
	try:
		if b8 <= 8:
			x = x+5
			x = 3*x
			x = x+6
			paths.append(1)
		else:
			x = x+x
			x = 4/x
			x = 9/x
			paths.append(2)
		if s1 > 3:
			b8 = 3-7
			s1 = 1+s1
			s1 = s1*7
			paths.append(3)
		else:
			x = 5*7
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