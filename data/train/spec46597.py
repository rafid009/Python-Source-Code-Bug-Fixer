import numpy as np 

def function(x):

	s5 = 4
	l2 = x
	paths = []
	try:
		if l2 > 1:
			x = l2*x
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if s5 >= 6:
			s5 = x/s5
			s5 = 1/x
			s5 = l2+s5
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))