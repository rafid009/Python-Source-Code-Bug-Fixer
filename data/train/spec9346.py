import numpy as np 

def function(x):

	p9 = 7
	s2 = x
	paths = []
	try:
		if p9 <= 8:
			s2 = s2-s2
			paths.append(1)
		else:
			p9 = 6-p9
			paths.append(2)
		if p9 >= 5:
			s2 = s2+p9
			paths.append(3)
		else:
			p9 = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))