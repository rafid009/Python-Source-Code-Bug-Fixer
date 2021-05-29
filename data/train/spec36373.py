import numpy as np 

def function(x):

	e7 = x
	s1 = 3
	paths = []
	try:
		if s1 > 6:
			e7 = e7*2
			paths.append(1)
		else:
			e7 = e7+6
			paths.append(2)
		if s1 > 4:
			e7 = e7-s1
			x = s1-8
			e7 = 8-e7
			paths.append(3)
		else:
			s1 = x/8
			s1 = s1+x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))