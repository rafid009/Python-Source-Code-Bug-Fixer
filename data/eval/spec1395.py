import numpy as np 

def function(x):

	l6 = 2
	s0 = x
	paths = []
	try:
		if x <= 1:
			l6 = x+0
			paths.append(1)
		else:
			l6 = s0+6
			s0 = s0-8
			paths.append(2)
		if l6 <= 7:
			s0 = x*5
			paths.append(3)
		else:
			s0 = s0+9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))