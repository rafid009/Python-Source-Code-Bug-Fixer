import numpy as np 

def function(x):

	b2 = 7
	s6 = x
	paths = []
	try:
		if s6 <= 9:
			b2 = b2*s6
			paths.append(1)
		else:
			s6 = s6*x
			s6 = s6+4
			paths.append(2)
		if b2 > 4:
			x = 4+8
			paths.append(3)
		else:
			x = x-5
			b2 = 5*x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		b2 = s6**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))