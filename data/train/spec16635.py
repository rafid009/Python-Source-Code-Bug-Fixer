import numpy as np 

def function(x):

	s6 = 0
	b2 = 4
	paths = []
	try:
		if x > 6:
			b2 = b2-4
			paths.append(1)
		else:
			b2 = b2*x
			x = 9/x
			x = x/6
			paths.append(2)
		if s6 >= 6:
			s6 = s6-4
			b2 = 1*b2
			b2 = 6/x
			paths.append(3)
		else:
			b2 = x+b2
			b2 = x+8
			s6 = s6-b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))