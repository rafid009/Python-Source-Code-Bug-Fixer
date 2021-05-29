import numpy as np 

def function(x):

	s5 = x
	l0 = x
	paths = []
	try:
		if l0 > 2:
			s5 = 4-s5
			paths.append(1)
		else:
			x = s5*5
			x = x/8
			paths.append(2)
		if s5 <= 0:
			l0 = l0*s5
			paths.append(3)
		else:
			l0 = 4+s5
			s5 = s5+1
			l0 = s5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))