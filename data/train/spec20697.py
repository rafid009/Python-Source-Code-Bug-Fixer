import numpy as np 

def function(x):

	b6 = 0
	s7 = 9
	paths = []
	try:
		if b6 <= 8:
			s7 = s7+x
			s7 = s7-6
			b6 = b6/5
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if s7 > 3:
			s7 = 5+4
			x = x-s7
			paths.append(3)
		else:
			s7 = 7*s7
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))