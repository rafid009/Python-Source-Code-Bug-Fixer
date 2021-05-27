import numpy as np 

def function(x):

	l0 = 3
	s6 = 2
	paths = []
	try:
		if s6 >= 7:
			l0 = 4+s6
			paths.append(1)
		else:
			l0 = x/l0
			paths.append(2)
		if l0 >= 7:
			x = 6/4
			paths.append(3)
		else:
			s6 = s6+4
			x = x+3
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))