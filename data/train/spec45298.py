import numpy as np 

def function(x):

	w2 = x
	s4 = x
	paths = []
	try:
		if x > 6:
			w2 = 7*5
			s4 = s4-w2
			paths.append(1)
		else:
			w2 = 1/w2
			s4 = s4/8
			x = 2*x
			paths.append(2)
		if s4 > 7:
			w2 = 0-6
			s4 = s4+5
			s4 = x+s4
			paths.append(3)
		else:
			s4 = s4+9
			x = w2/2
			w2 = 9/w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))