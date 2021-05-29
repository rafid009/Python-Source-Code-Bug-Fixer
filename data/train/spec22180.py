import numpy as np 

def function(x):

	w8 = x
	s2 = 8
	paths = []
	try:
		if x > 4:
			s2 = 3+x
			s2 = 8-s2
			s2 = w8*s2
			paths.append(1)
		else:
			s2 = 8-s2
			s2 = x-2
			x = 2/x
			paths.append(2)
		if w8 > 8:
			w8 = s2-8
			s2 = 5/2
			paths.append(3)
		else:
			w8 = 7-s2
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		s2 = w8**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))