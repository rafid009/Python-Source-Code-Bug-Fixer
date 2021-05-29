import numpy as np 

def function(x):

	r7 = x
	s2 = 9
	paths = []
	try:
		if s2 <= 6:
			x = r7/6
			r7 = x*s2
			paths.append(1)
		else:
			s2 = 8/s2
			s2 = s2*s2
			paths.append(2)
		if r7 >= 8:
			s2 = s2+6
			r7 = r7*7
			paths.append(3)
		else:
			x = 1+2
			s2 = r7*x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		s2 = r7**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))