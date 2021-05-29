import numpy as np 

def function(x):

	l0 = x
	s5 = x
	paths = []
	try:
		if s5 <= 4:
			s5 = 1+s5
			paths.append(1)
		else:
			x = 1/x
			l0 = 2-7
			paths.append(2)
		if l0 > 6:
			x = x-4
			paths.append(3)
		else:
			s5 = 8/s5
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