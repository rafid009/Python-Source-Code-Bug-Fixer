import numpy as np 

def function(x):

	b5 = 4
	s6 = 6
	paths = []
	try:
		if b5 >= 0:
			s6 = 1+b5
			s6 = s6*1
			s6 = 5*s6
			paths.append(1)
		else:
			s6 = s6+0
			b5 = 6+8
			paths.append(2)
		if s6 < 6:
			s6 = s6/3
			b5 = 1-8
			paths.append(3)
		else:
			b5 = s6+0
			s6 = s6*s6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))