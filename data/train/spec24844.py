import numpy as np 

def function(x):

	s2 = 6
	a1 = x
	paths = []
	try:
		if x <= 9:
			s2 = 1+8
			x = x*8
			paths.append(1)
		else:
			x = 4*x
			a1 = x/a1
			paths.append(2)
		if a1 >= 9:
			a1 = a1+4
			s2 = s2/x
			a1 = a1+x
			paths.append(3)
		else:
			x = x/6
			s2 = s2-8
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		s2 = a1**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))