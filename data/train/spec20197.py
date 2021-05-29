import numpy as np 

def function(x):

	s6 = x
	l6 = 4
	paths = []
	try:
		if l6 > 8:
			x = s6+x
			x = x+1
			x = x/8
			paths.append(1)
		else:
			l6 = x-1
			x = 0-l6
			paths.append(2)
		if x > 7:
			s6 = 4*s6
			l6 = l6*6
			l6 = 0/7
			paths.append(3)
		else:
			x = 9*s6
			l6 = 1/l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))