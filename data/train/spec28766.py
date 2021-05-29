import numpy as np 

def function(x):

	p9 = x
	s7 = 7
	paths = []
	try:
		if x <= 1:
			x = 9+x
			p9 = 0/s7
			paths.append(1)
		else:
			p9 = p9+5
			paths.append(2)
		if p9 >= 6:
			p9 = p9/3
			s7 = s7/1
			x = p9+x
			paths.append(3)
		else:
			p9 = 9*p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))