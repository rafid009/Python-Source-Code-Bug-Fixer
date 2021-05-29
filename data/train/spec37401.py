import numpy as np 

def function(x):

	s1 = 2
	e6 = x
	paths = []
	try:
		if x >= 6:
			s1 = 3-x
			x = 2*e6
			paths.append(1)
		else:
			s1 = 3+8
			e6 = 6+x
			paths.append(2)
		if e6 > 1:
			s1 = 0+s1
			x = 4*s1
			paths.append(3)
		else:
			e6 = e6-7
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))