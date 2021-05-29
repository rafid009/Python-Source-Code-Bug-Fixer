import numpy as np 

def function(x):

	q8 = 7
	s7 = 2
	paths = []
	try:
		if s7 < 2:
			s7 = s7*9
			s7 = 2*s7
			x = 9*2
			paths.append(1)
		else:
			s7 = 6+s7
			paths.append(2)
		if x > 5:
			q8 = 2-q8
			s7 = s7-x
			q8 = q8-8
			paths.append(3)
		else:
			s7 = 6+3
			s7 = 7-q8
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))