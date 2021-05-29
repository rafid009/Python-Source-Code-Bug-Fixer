import numpy as np 

def function(x):

	s2 = 7
	b2 = x
	paths = []
	try:
		if s2 > 7:
			x = x-s2
			s2 = s2/8
			b2 = 3-6
			paths.append(1)
		else:
			x = s2*b2
			b2 = b2+1
			paths.append(2)
		if b2 >= 6:
			x = 4*x
			b2 = s2/s2
			paths.append(3)
		else:
			s2 = s2*x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		b2 = s2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))