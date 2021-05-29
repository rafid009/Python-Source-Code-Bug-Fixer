import numpy as np 

def function(x):

	l8 = x
	s2 = x
	paths = []
	try:
		if x >= 4:
			l8 = l8/2
			s2 = 6*s2
			s2 = 4/5
			paths.append(1)
		else:
			s2 = s2+5
			l8 = l8+s2
			paths.append(2)
		if s2 <= 2:
			s2 = 8/s2
			s2 = s2*s2
			paths.append(3)
		else:
			l8 = s2*l8
			x = x*x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))