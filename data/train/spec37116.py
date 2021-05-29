import numpy as np 

def function(x):

	l0 = x
	s2 = 5
	paths = []
	try:
		if x > 8:
			s2 = 1-s2
			l0 = s2-l0
			s2 = 4+0
			paths.append(1)
		else:
			x = x+8
			s2 = l0*x
			paths.append(2)
		if l0 < 4:
			s2 = 6/l0
			paths.append(3)
		else:
			l0 = l0/9
			x = l0+3
			l0 = x-s2
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