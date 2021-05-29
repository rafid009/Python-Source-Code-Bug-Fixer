import numpy as np 

def function(x):

	l4 = x
	s1 = 2
	x = x
	paths = []
	try:
		if s1 > 4:
			x = 3-x
			l4 = x+9
			l4 = l4*2
			paths.append(1)
		else:
			x = l4*4
			paths.append(2)
		if s1 >= 7:
			l4 = 5+l4
			l4 = 5/7
			l4 = l4/9
			paths.append(3)
		else:
			x = x-1
			l4 = 0+l4
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