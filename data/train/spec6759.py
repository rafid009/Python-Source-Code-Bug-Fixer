import numpy as np 

def function(x):

	s4 = 5
	b2 = x
	paths = []
	try:
		if s4 > 9:
			x = s4*8
			x = s4+x
			x = x/x
			paths.append(1)
		else:
			s4 = s4/9
			b2 = 3+b2
			paths.append(2)
		if x > 2:
			s4 = x-s4
			s4 = s4+1
			paths.append(3)
		else:
			b2 = x+6
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		s4 = b2**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))